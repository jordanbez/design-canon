#!/usr/bin/env python3
"""
refresh_meta.py - recompute every number in the skill and patch it into README.md + SKILL.md.

Fully offline. Counts, the per-theme routing table and the coverage window are all derived
from references/*.md, so the published numbers can never disagree with the content.

    python3 pipeline/refresh_meta.py --check              # preview, write nothing
    python3 pipeline/refresh_meta.py                      # patch the files
    python3 pipeline/refresh_meta.py --updated 2026-09-01 # also bump the "last updated" date

Each theme file describes itself in its own header, which is what feeds the routing table:

    # UX Laws
    <!-- covers: attention, memory, decision time, Gestalt grouping -->
"""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

import skill_lib as sl

H1_RE = re.compile(r"^#\s+(?P<title>.+?)\s*$", re.M)
COVERS_RE = re.compile(r"<!--\s*covers:\s*(?P<covers>.+?)\s*-->")


def block(name: str, body: str, text: str) -> str:
    """Replace everything between <!-- meta:name --> and <!-- /meta:name -->."""
    rx = re.compile(rf"(<!--\s*meta:{name}\s*-->)(.*?)(<!--\s*/meta:{name}\s*-->)", re.S)
    if not rx.search(text):
        return text
    return rx.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(3)}", text)


def theme_meta() -> list[dict]:
    out = []
    counts = sl.counts_by_theme()
    for p in sl.theme_files():
        head = p.read_text(encoding="utf-8")[:2000]
        t = H1_RE.search(head)
        c = COVERS_RE.search(head)
        out.append({
            "slug": p.stem,
            "title": t.group("title") if t else p.stem.replace("-", " ").title(),
            "covers": c.group("covers") if c else "",
            "count": counts.get(p.stem, 0),
        })
    return sorted(out, key=lambda d: -d["count"])


# README.md sits at the repo root; the skill it documents lives one level down.
README_PREFIX = "skills/design-canon/"


def render_readme_table(themes: list[dict]) -> str:
    rows = ["| Theme | Entries | Covers |", "| --- | ---: | --- |"]
    for t in themes:
        rows.append(f"| [{t['title']}]({README_PREFIX}references/{t['slug']}.md) | {t['count']} | {t['covers']} |")
    return "\n".join(rows)


def render_routing_table(themes: list[dict]) -> str:
    rows = ["| When the question is about... | Open |", "| --- | --- |"]
    for t in themes:
        rows.append(f"| {t['covers'] or t['title']} | [{t['slug']}](references/{t['slug']}.md) |")
    return "\n".join(rows)


def render_badges(total: int, themes: int, sources: int, updated: str) -> str:
    return (
        "![Agent Skill](https://img.shields.io/badge/Agent-Skill-5b4ee6)\n"
        f"![Principles](https://img.shields.io/badge/principles-{total}-2ea44f)\n"
        f"![Themes](https://img.shields.io/badge/themes-{themes}-2ea44f)\n"
        f"![Sources](https://img.shields.io/badge/sources-{sources}-2ea44f)\n"
        f"![Updated](https://img.shields.io/badge/updated-{updated.replace('-', '--')}-e67e22)"
    )


def render_sources(counts: dict[str, int]) -> str:
    return "\n".join(f"- **{name}** - {n} entr{'y' if n == 1 else 'ies'}" for name, n in counts.items())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="preview without writing")
    ap.add_argument("--updated", help="YYYY-MM-DD to stamp as the last-updated date")
    args = ap.parse_args()

    entries = sl.all_entries()
    themes = theme_meta()
    srcs = sl.source_names()
    lo, hi = sl.coverage_window(entries)
    updated = args.updated or date.today().isoformat()
    coverage = (f"Distilled entries span **{lo} to {hi}** where the source is dated; "
                f"undated canonical references carry no date."
                if lo else "Coverage dates are attached to entries whose source page is dated.")

    print(f"entries {len(entries)} | themes {len(themes)} | sources {len(srcs)} | updated {updated}")
    for t in themes:
        print(f"  {t['slug']:<32} {t['count']:>4}")
    if args.check:
        print("\n--check: nothing written.")
        return 0

    patches = {
        sl.ROOT / "README.md": [
            ("badges", render_badges(len(entries), len(themes), len(srcs), updated)),
            ("themes", render_readme_table(themes)),
            ("coverage", coverage),
            ("sources", render_sources(srcs)),
            ("count", str(len(entries))),
        ],
        sl.SKILL_DIR / "SKILL.md": [
            ("routing", render_routing_table(themes)),
            ("count", str(len(entries))),
        ],
    }

    for path, blocks in patches.items():
        if not path.exists():
            print(f"  ! {path.name} not found, skipped")
            continue
        text = original = path.read_text(encoding="utf-8")
        for name, body in blocks:
            text = block(name, body, text)
        text = re.sub(r"(?<=updated-)\d{4}--\d{2}--\d{2}", updated.replace("-", "--"), text)
        if text != original:
            path.write_text(text, encoding="utf-8")
            print(f"  patched {path.name}")
        else:
            print(f"  {path.name} already current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
