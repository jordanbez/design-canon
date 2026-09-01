#!/usr/bin/env python3
"""
extract.py - fetch a URL and turn it into clean, agent-readable markdown.

Stdlib only. Deliberately conservative: it drops chrome (nav, footer, script, forms),
keeps structure (headings, lists, blockquotes, links) and reports the publication date
when the page exposes one. Good enough to hand an article to a model for distillation;
it is not a general-purpose readability engine.
"""

from __future__ import annotations

import gzip
import re
import time
import zlib
from dataclasses import dataclass, field
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit
from urllib.request import Request, urlopen

UA = "Mozilla/5.0 (compatible; design-canon-bot/1.0; +https://github.com/jordanbez/design-canon)"

DROP = {"script", "style", "noscript", "nav", "footer", "aside", "form",
        "svg", "iframe", "button", "select", "template", "picture"}
HEADINGS = {"h1": "#", "h2": "##", "h3": "###", "h4": "####", "h5": "#####", "h6": "######"}
BLOCKS = {"p", "div", "section", "article", "main", "ul", "ol", "table", "tr",
          "figcaption", "blockquote", "pre", "header"}

DATE_META = ("article:published_time", "datePublished", "publish_date", "date",
             "og:published_time", "article:modified_time")
DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


def fetch(url: str, timeout: int = 30, retries: int = 3) -> str:
    """GET a URL and return decoded text. Retries on transient failure."""
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = Request(url, headers={
                "User-Agent": UA,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate",
            })
            with urlopen(req, timeout=timeout) as resp:
                raw = resp.read()
                enc = (resp.headers.get("Content-Encoding") or "").lower()
                if enc == "gzip":
                    raw = gzip.decompress(raw)
                elif enc == "deflate":
                    raw = zlib.decompress(raw, -zlib.MAX_WBITS)
                charset = resp.headers.get_content_charset() or "utf-8"
                return raw.decode(charset, errors="replace")
        except Exception as exc:  # noqa: BLE001 - report the last failure to the caller
            last = exc
            if attempt < retries - 1:
                time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"fetch failed for {url}: {last}")


@dataclass
class Page:
    url: str
    title: str = ""
    description: str = ""
    published: str = ""
    text: str = ""
    links: list[tuple[str, str]] = field(default_factory=list)


class _Reader(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base = base_url
        self.page = Page(url=base_url)
        self._drop_depth = 0
        self._out: list[str] = []
        self._in_title = False
        self._href: str | None = None
        self._link_buf: list[str] = []
        self._list_stack: list[str] = []
        self._in_pre = False

    # -- helpers -------------------------------------------------------------
    def _emit(self, s: str) -> None:
        (self._link_buf if self._href is not None else self._out).append(s)

    def _newline(self, n: int = 1) -> None:
        if self._href is None:
            self._out.append("\n" * n)

    # -- parser hooks --------------------------------------------------------
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in DROP:
            self._drop_depth += 1
            return
        if self._drop_depth:
            return
        if tag == "title":
            self._in_title = True
        elif tag == "meta":
            key = (a.get("property") or a.get("name") or a.get("itemprop") or "").strip()
            content = (a.get("content") or "").strip()
            if key in ("description", "og:description") and not self.page.description:
                self.page.description = content
            if key in DATE_META and not self.page.published:
                m = DATE_RE.search(content)
                if m:
                    self.page.published = m.group(0)
        elif tag == "time":
            m = DATE_RE.search(a.get("datetime", ""))
            if m and not self.page.published:
                self.page.published = m.group(0)
        elif tag in HEADINGS:
            self._newline(2)
            self._emit(HEADINGS[tag] + " ")
        elif tag == "li":
            self._newline()
            self._emit("1. " if (self._list_stack and self._list_stack[-1] == "ol") else "- ")
        elif tag in ("ul", "ol"):
            self._list_stack.append(tag)
            self._newline(2)
        elif tag == "blockquote":
            self._newline(2)
            self._emit("> ")
        elif tag == "pre":
            self._in_pre = True
            self._newline(2)
            self._emit("```\n")
        elif tag == "a":
            href = a.get("href", "")
            if href and not href.startswith(("#", "javascript:", "mailto:")):
                self._href = urljoin(self.base, href)
                self._link_buf = []
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "code" and not self._in_pre:
            self._emit("`")
        elif tag == "br":
            self._newline()
        elif tag in BLOCKS:
            self._newline(2)

    def handle_endtag(self, tag):
        if tag in DROP:
            self._drop_depth = max(0, self._drop_depth - 1)
            return
        if self._drop_depth:
            return
        if tag == "title":
            self._in_title = False
        elif tag in HEADINGS or tag in BLOCKS:
            if tag == "pre":
                self._in_pre = False
                self._emit("\n```")
            if tag in ("ul", "ol") and self._list_stack:
                self._list_stack.pop()
            self._newline(2)
        elif tag == "a" and self._href is not None:
            label = re.sub(r"\s+", " ", "".join(self._link_buf)).strip()
            href, self._href, self._link_buf = self._href, None, []
            if label:
                self.page.links.append((href, label))
                self._out.append(f"[{label}]({href})")
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "code" and not self._in_pre:
            self._emit("`")

    def handle_data(self, data):
        if self._drop_depth:
            return
        if self._in_title:
            self.page.title += data.strip()
            return
        if self._in_pre:
            self._emit(data)
            return
        text = re.sub(r"[ \t\r\f\v]+", " ", data.replace("\n", " "))
        if text.strip() or (text == " " and (self._out or self._link_buf)):
            self._emit(text)

    def result(self) -> Page:
        body = "".join(self._out)
        body = re.sub(r"[ \t]+", " ", body)
        body = re.sub(r" *\n *", "\n", body)
        body = re.sub(r"\n{3,}", "\n\n", body).strip()
        self.page.text = body
        self.page.title = re.sub(r"\s+", " ", self.page.title).strip()
        return self.page


def parse(html: str, url: str) -> Page:
    r = _Reader(url)
    r.feed(html)
    return r.result()


def read(url: str) -> Page:
    return parse(fetch(url), url)


def index_links(url: str, item_pattern: str | None) -> list[tuple[str, str]]:
    """Fetch an index page and return (absolute_url, label) for every link whose PATH
    matches item_pattern. Pattern is matched against the path only, so it stays readable."""
    page = read(url)
    if not item_pattern:
        return [(url, page.title)]
    rx = re.compile(item_pattern)
    host = urlsplit(url).netloc
    out, seen = [], set()
    for href, label in page.links:
        parts = urlsplit(href)
        if parts.netloc != host or not rx.match(parts.path):
            continue
        key = parts.path.rstrip("/")
        if key in seen:
            continue
        seen.add(key)
        out.append((href, label))
    return out


def feed_items(url: str) -> list[tuple[str, str]]:
    """Parse an RSS or Atom feed into (link, title) pairs."""
    import xml.etree.ElementTree as ET

    root = ET.fromstring(fetch(url))
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out: list[tuple[str, str]] = []
    for item in root.iter():
        tag = item.tag.split("}")[-1]
        if tag not in ("item", "entry"):
            continue
        link = item.findtext("link") or ""
        if not link:
            el = item.find("a:link", ns)
            link = el.get("href", "") if el is not None else ""
        title = (item.findtext("title") or item.findtext("a:title", default="", namespaces=ns) or "").strip()
        if link:
            out.append((link.strip(), title))
    return out


if __name__ == "__main__":
    import sys
    p = read(sys.argv[1])
    print(f"# {p.title}\n<{p.url}>  published={p.published or '-'}\n")
    print(p.text[:3000])
