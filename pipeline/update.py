#!/usr/bin/env python3
"""
update.py - fetch every not-yet-covered item and stage a ready-to-run distillation prompt.

    python3 pipeline/update.py                    # watch sources
    python3 pipeline/update.py --seed
    python3 pipeline/update.py --source laws-of-ux
    python3 pipeline/update.py --from new.json    # reuse a discover.py --json report

For each new item it writes:
    pipeline/staging/posts/<slug>.md      the normalised article
    pipeline/staging/prompts/<slug>.md    distill spec + license tier + article, ready to paste

Nothing here writes to references/. A human always reviews the distilled entry before
it enters the skill - that review is the whole quality gate.
"""

from __future__ import annotations

import argparse
import json
import sys

import discover
import extract
import skill_lib as sl

SPEC = sl.PIPELINE / "prompts" / "distill.md"


def stage_one(item: dict, spec: str) -> str | None:
    try:
        page = extract.read(item["url"])
    except Exception as exc:  # noqa: BLE001
        print(f"  x {item['url']}: {exc}", file=sys.stderr)
        return None

    slug = sl.slugify(f"{item['source']}-{page.title or item['title']}")
    tier = sl.LICENSE_TIERS[item["license"]]
    date_label = page.published or "(no date on page - omit the date from the Source line)"

    body = (
        f"# {page.title or item['title']}\n\n"
        f"- URL: {item['url']}\n"
        f"- Source name: {item['name']}\n"
        f"- Published: {date_label}\n"
        f"- License tier: {item['license'].upper()} - {tier}\n\n"
        f"{page.description}\n\n---\n\n{page.text}\n"
    )
    (sl.STAGING / "posts" / f"{slug}.md").write_text(body, encoding="utf-8")

    prompt = (
        spec
        + "\n\n---\n\n# ITEM TO DISTILL\n\n"
        + f"Target file: `references/{item['theme']}.md`\n"
        + f"Source label to use: `{item['name']}"
        + (f" - {page.published}" if page.published else "")
        + "`\n"
        + f"License tier: **{item['license'].upper()}** - {tier}\n\n"
        + "---\n\n"
        + body
    )
    (sl.STAGING / "prompts" / f"{slug}.md").write_text(prompt, encoding="utf-8")
    return slug


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", action="store_true")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--source")
    ap.add_argument("--from", dest="from_json", help="a discover.py --json report")
    ap.add_argument("--limit", type=int, default=0, help="stage at most N items")
    args = ap.parse_args()

    if not SPEC.exists():
        print(f"missing distillation spec: {SPEC}", file=sys.stderr)
        return 2
    spec = SPEC.read_text(encoding="utf-8")

    if args.from_json:
        report = json.loads(open(args.from_json, encoding="utf-8").read())
        items = [i for s in report["sources"] for i in s.get("new", [])]
    else:
        if args.source:
            sources = [s for s in sl.load_sources() if s["id"] == args.source and s["mode"] != "roadmap"]
        elif args.all:
            sources = sl.sources_by_mode("watch", "seed")
        elif args.seed:
            sources = sl.sources_by_mode("seed")
        else:
            sources = sl.sources_by_mode("watch")
        have = sl.included_urls()
        items = []
        for s in sources:
            try:
                found = discover.candidates(s)
            except Exception as exc:  # noqa: BLE001
                print(f"  ! {s['id']}: {exc}", file=sys.stderr)
                continue
            for u, t in found:
                if sl.normalize_url(u) not in have:
                    items.append({"url": u, "title": t, "source": s["id"], "name": s["name"],
                                  "theme": s["theme"], "license": s["license"]})

    if args.limit:
        items = items[: args.limit]
    if not items:
        print("Nothing new. The skill already covers every discoverable item.")
        return 0

    for d in ("posts", "prompts"):
        (sl.STAGING / d).mkdir(parents=True, exist_ok=True)

    print(f"Staging {len(items)} item(s)...")
    staged = [s for s in (stage_one(i, spec) for i in items) if s]
    for s in staged:
        print(f"  + {s}")

    print(f"\nStaged {len(staged)}/{len(items)} under pipeline/staging/")
    print("\nNext, in Claude Code from the repo root:")
    print('  "Read every file in pipeline/staging/prompts/, produce the finished entry for each')
    print('   following the spec exactly, tell me which references/<theme>.md it belongs in,')
    print('   and wait for my OK before writing anything."')
    print("\nThen: python3 pipeline/refresh_meta.py --updated $(date +%F)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
