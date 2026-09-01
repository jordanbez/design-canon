#!/usr/bin/env python3
"""
discover.py - list source items that are NOT yet distilled into the skill.

The baseline is the skill itself (see skill_lib: "the skill is its own manifest"),
so this never needs a state file and re-running is always safe.

    python3 pipeline/discover.py                 # watch sources only (what the cron runs)
    python3 pipeline/discover.py --seed          # bulk corpus sources
    python3 pipeline/discover.py --all
    python3 pipeline/discover.py --source laws-of-ux
    python3 pipeline/discover.py --json          # machine-readable, for the workflow

Sources with mode "roadmap" are never discovered - they are deliberately excluded
(see the license tiers in sources.json).
"""

from __future__ import annotations

import argparse
import json
import sys

import extract
import skill_lib as sl


def candidates(source: dict) -> list[tuple[str, str]]:
    how = source.get("discovery", "html-index")
    url = source["index"]
    if how == "single":
        return [(url, source["name"])]
    if how == "rss":
        return extract.feed_items(url)
    return extract.index_links(url, source.get("item_pattern"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", action="store_true", help="discover seed sources instead of watch")
    ap.add_argument("--all", action="store_true", help="discover watch + seed sources")
    ap.add_argument("--source", help="a single source id from sources.json")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args()

    if args.source:
        sources = [s for s in sl.load_sources() if s["id"] == args.source]
        if not sources:
            print(f"unknown source id: {args.source}", file=sys.stderr)
            return 2
        if sources[0]["mode"] == "roadmap":
            print(f"'{args.source}' is mode=roadmap and is deliberately excluded. "
                  f"Reason: {sources[0]['notes']}", file=sys.stderr)
            return 2
    elif args.all:
        sources = sl.sources_by_mode("watch", "seed")
    elif args.seed:
        sources = sl.sources_by_mode("seed")
    else:
        sources = sl.sources_by_mode("watch")

    have = sl.included_urls()
    report, total, failed = [], 0, 0

    for s in sources:
        try:
            found = candidates(s)
        except Exception as exc:  # noqa: BLE001 - one broken source must not kill the run
            failed += 1
            report.append({"id": s["id"], "error": str(exc), "new": []})
            print(f"  ! {s['id']}: {exc}", file=sys.stderr)
            continue
        new = [
            {"url": u, "title": t, "source": s["id"], "name": s["name"],
             "theme": s["theme"], "license": s["license"]}
            for u, t in found
            if sl.normalize_url(u) not in have
        ]
        seen, deduped = set(), []
        for item in new:
            k = sl.normalize_url(item["url"])
            if k not in seen:
                seen.add(k)
                deduped.append(item)
        total += len(deduped)
        report.append({"id": s["id"], "name": s["name"], "theme": s["theme"],
                       "license": s["license"], "found": len(found), "new": deduped})

    if args.json:
        print(json.dumps({"total_new": total, "failed": failed,
                          "checked": len(sources), "sources": report}, indent=2))
        return 2 if failed == len(sources) and sources else 0

    print(f"Already in the skill: {len(have)} source URLs across {len(sl.theme_files())} themes\n")
    for r in report:
        if "error" in r:
            print(f"{r['id']:<34} ERROR  {r['error']}")
            continue
        mark = "+" if r["new"] else " "
        print(f"{mark} {r['id']:<32} {len(r['new']):>3} new / {r['found']:>3} found  "
              f"[{r['license']}] -> references/{r['theme']}.md")
        for item in r["new"]:
            print(f"      {item['title'][:70] or '(no title)'}")
            print(f"      {item['url']}")
    if failed == len(sources) and sources:
        print(f"\nEVERY source failed ({failed}/{len(sources)}). This is a connectivity or\nselector problem, NOT an empty result - do not read it as \"nothing new\".", file=sys.stderr)
        return 2
    if failed:
        print(f"\n{failed} of {len(sources)} source(s) failed; the count below covers the rest.",
              file=sys.stderr)
    print(f"\nTOTAL NEW: {total}")
    if total:
        print("Next: python3 pipeline/update.py   (fetches + stages a distillation prompt for each)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
