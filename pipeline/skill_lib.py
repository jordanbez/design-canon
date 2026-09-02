#!/usr/bin/env python3
"""
skill_lib.py - shared helpers for the design-canon maintainer pipeline.

CORE IDEA: THE SKILL IS ITS OWN MANIFEST.
There is no separate "what have we already covered" state file that could drift.
Coverage is derived from the `**Source.**` lines inside references/*.md, so counts,
coverage windows and delta detection are computed from the actual content, offline,
with zero network requests.

Source line shape (the date is optional - undated canonical pages omit it):
    **Source.** [Laws of UX - Jakob's Law](https://lawsofux.com/jakobs-law/)
    **Source.** [Humane by Design - 2024-01-23](https://humanebydesign.com/articles/the-cost-of-personalization/)

Stdlib only, on purpose: the pipeline must run with a bare `python3`, no pip install.
"""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterator
from urllib.parse import unquote, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parent.parent
# Only SKILL_DIR ships to an installing agent. Everything else here is maintainer
# tooling and must stay out of it - see AGENT.md.
SKILL_DIR = ROOT / "skills" / "design-canon"
REFERENCES = SKILL_DIR / "references"
ASSETS = SKILL_DIR / "assets"
PIPELINE = ROOT / "pipeline"
STAGING = PIPELINE / "staging"
SOURCES_FILE = PIPELINE / "sources.json"

SOURCE_RE = re.compile(r"^\*\*Source\.\*\*\s*\[(?P<label>[^\]]+)\]\((?P<url>[^)\s]+)\)", re.M)
TITLE_RE = re.compile(r"^##\s+(?P<title>.+?)\s*$", re.M)
DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")

LICENSE_TIERS = {
    "green": "Openly licensed or explicitly permissive. Distill freely with attribution; "
             "informational assets may be mirrored into assets/.",
    "amber": "Free to read, all rights reserved. Distill the idea in your own words and link "
             "the source. Never reproduce the original prose verbatim, never mirror images.",
    "red":   "The content IS the product being sold. Excluded from the corpus until the "
             "publisher grants reuse permission. See the roadmap in README.md.",
}


def normalize_url(url: str) -> str:
    """Canonical form used for delta detection: https, no www, percent-decoded,
    no query, no fragment, no trailing slash."""
    parts = urlsplit(url.strip())
    host = (parts.netloc or "").lower()
    if host.startswith("www."):
        host = host[4:]
    path = unicodedata.normalize("NFC", unquote(parts.path or "")).rstrip("/")
    return urlunsplit(("https", host, path, "", ""))


def slugify(text: str, maxlen: int = 60) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text[:maxlen].strip("-") or "untitled"


@dataclass(frozen=True)
class Entry:
    """One distilled principle in a references/<theme>.md file."""
    title: str
    theme: str
    label: str
    url: str
    url_norm: str
    published: date | None

    @property
    def source_name(self) -> str:
        return self.label.split(" - ")[0].split(" · ")[0].strip()


def parse_theme_file(path: Path) -> list[Entry]:
    text = path.read_text(encoding="utf-8")
    titles = [(m.start(), m.group("title")) for m in TITLE_RE.finditer(text)]
    entries: list[Entry] = []
    for m in SOURCE_RE.finditer(text):
        title = "(untitled)"
        for pos, t in titles:
            if pos < m.start():
                title = t
            else:
                break
        label = m.group("label").strip()
        d = DATE_RE.search(label)
        entries.append(
            Entry(
                title=title,
                theme=path.stem,
                label=label,
                url=m.group("url").strip(),
                url_norm=normalize_url(m.group("url")),
                published=date(int(d.group(1)), int(d.group(2)), int(d.group(3))) if d else None,
            )
        )
    return entries


def theme_files() -> list[Path]:
    return sorted(p for p in REFERENCES.glob("*.md") if not p.name.startswith("_"))


def all_entries() -> list[Entry]:
    out: list[Entry] = []
    for p in theme_files():
        out.extend(parse_theme_file(p))
    return out


def included_urls() -> set[str]:
    """Every source URL already distilled into the skill. This is the delta baseline."""
    return {e.url_norm for e in all_entries()}


def counts_by_theme() -> dict[str, int]:
    return {p.stem: len(parse_theme_file(p)) for p in theme_files()}


def coverage_window(entries: list[Entry] | None = None) -> tuple[date | None, date | None]:
    dates = sorted(e.published for e in (entries or all_entries()) if e.published)
    return (dates[0], dates[-1]) if dates else (None, None)


def source_names() -> dict[str, int]:
    counts: dict[str, int] = {}
    for e in all_entries():
        counts[e.source_name] = counts.get(e.source_name, 0) + 1
    return dict(sorted(counts.items(), key=lambda kv: -kv[1]))


def load_sources() -> list[dict]:
    return json.loads(SOURCES_FILE.read_text(encoding="utf-8"))["sources"]


def sources_by_mode(*modes: str) -> list[dict]:
    return [s for s in load_sources() if s.get("mode") in modes]


def iter_new(candidates: Iterator[tuple[str, str]]) -> list[tuple[str, str]]:
    """Filter (url, title) candidates down to the ones not already in the skill."""
    have = included_urls()
    seen: set[str] = set()
    new: list[tuple[str, str]] = []
    for url, title in candidates:
        n = normalize_url(url)
        if n in have or n in seen:
            continue
        seen.add(n)
        new.append((url, title))
    return new


def undiscoverable_entries() -> list[tuple[str, str]]:
    """Entries whose own source could no longer discover them.

    The skill is its own manifest, so an already-distilled URL that its source's
    `item_pattern` does not match proves the pattern is too tight - and a pattern
    that is too tight fails silently, reporting "nothing new" forever. Checking the
    patterns against the corpus is the only feedback that failure mode ever gives.
    Returns (url, reason) pairs; empty means every pattern still reaches its content.
    """
    by_host: dict[str, list[dict]] = {}
    for s in load_sources():
        by_host.setdefault(urlsplit(normalize_url(s["index"])).netloc, []).append(s)

    def reaches(src: dict, url: str, path: str) -> bool:
        if src.get("discovery") == "single":
            return url == normalize_url(src["index"])
        pattern = src.get("item_pattern")
        return bool(pattern) and re.match(pattern, path + "/") is not None

    bad: list[tuple[str, str]] = []
    for e in all_entries():
        parts = urlsplit(e.url_norm)
        srcs = by_host.get(parts.netloc, [])
        if not srcs:
            bad.append((e.url_norm, f"no source in sources.json covers {parts.netloc}"))
        elif not any(reaches(s, e.url_norm, parts.path) for s in srcs):
            ids = ", ".join(s["id"] for s in srcs)
            bad.append((e.url_norm, f"no item_pattern matches ({ids})"))
    return bad


if __name__ == "__main__":
    entries = all_entries()
    lo, hi = coverage_window(entries)
    print(f"entries      : {len(entries)}")
    print(f"themes       : {len(theme_files())}")
    for theme, n in sorted(counts_by_theme().items()):
        print(f"  {theme:<32} {n:>4}")
    print(f"coverage     : {lo or '-'} -> {hi or '-'}")
    print("sources      :")
    for name, n in source_names().items():
        print(f"  {name:<32} {n:>4}")

    broken = undiscoverable_entries()
    print(f"patterns     : {'OK' if not broken else str(len(broken)) + ' UNREACHABLE'}")
    for url, why in broken:
        print(f"  ! {url}\n    {why}")
    assert not broken, "sources.json patterns no longer reach the distilled corpus"
