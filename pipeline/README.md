# pipeline/ - keeping design-canon current

This folder is the machinery that builds the skill and keeps it in step with its sources.
It is **not part of the installed skill**: `npx skills add` and the agent only ever read
`SKILL.md`, `references/` and `assets/` at the repo root. Everything here is maintainer tooling.

Stdlib-only Python 3.10+. There is nothing to `pip install`.

## The core idea: the skill is its own manifest

There is no separate list of what has been ingested. The set of covered items is derived from
the `**Source.**` links at the bottom of every entry in `references/*.md`, so **coverage and
counts are computed offline and can never drift from the actual content**. Delete an entry and
the item becomes discoverable again, automatically.

This idea is borrowed from
[heliocosta-dev/revenue-centric-design](https://github.com/heliocosta-dev/revenue-centric-design),
which derives the same thing from tweet ids. Web sources have no equivalent of a Snowflake id,
so the date is carried explicitly in the source label instead:

```
**Source.** [Humane by Design - 2024-01-23](https://humanebydesign.com/articles/the-cost-of-personalization/)
**Source.** [Laws of UX - Jakob's Law](https://lawsofux.com/jakobs-law/)
```

Undated canonical pages use a distinguishing sub-label instead of a date. URLs are normalised
before comparison (https, no www, percent-decoded, no query, no trailing slash), so a link
written either way still matches.

## The loop

```
discover.py  ->  update.py  ->  distill in Claude Code + REVIEW  ->  paste into references/  ->  refresh_meta.py  ->  commit
 (what's new)   (fetch+stage)        (the taste and accuracy gate)         (the curation call)      (sync numbers)
```

1. **See what is new.** `python3 pipeline/discover.py` lists items on the watched sites that
   the skill does not cover. Add `--seed` for the bulk corpus sources, `--all` for both, or
   `--source <id>` for one. It applies no topical filter: it returns candidates, and curation
   is your call in step 3.

2. **Fetch and stage.** `python3 pipeline/update.py` writes, per new item:
   - `staging/posts/<slug>.md` - the normalised article
   - `staging/prompts/<slug>.md` - the distillation spec, the license tier, and the article,
     pre-assembled so it can be handed to a model as-is

3. **Distill, then review.** In Claude Code, from the repo root:

   > Read every file in `pipeline/staging/prompts/`, produce the finished entry for each
   > following the spec exactly, tell me which `references/<theme>.md` it belongs in, and
   > wait for my OK before writing anything.

   Not every candidate belongs. This is a curated corpus, so choose deliberately, and read
   every draft. The spec is strict, but you are the taste and accuracy check.

4. **Merge.** Paste each approved entry into the right `references/<theme>.md`, respecting
   that file's declared `<!-- order: -->`. If an entry keeps an image, and only if the source
   is GREEN tier, copy it into `../assets/` and reference it as `../assets/<file>`.

5. **Sync the numbers.** `python3 pipeline/refresh_meta.py --updated $(date +%F)` recomputes
   counts, the per-theme table, the routing table and the coverage window, and patches
   `README.md` and `SKILL.md`. Use `--check` first to preview. Add a `CHANGELOG.md` line and commit.

The weekly `watch-sources.yml` workflow runs steps 1 and 2 for you and opens a pull request
carrying the staged prompts, so in practice the loop starts at step 3.

## License tiers are enforced, not advisory

Every source in `sources.json` carries a tier, and it is stamped into each staged prompt.

| Tier | What may be produced |
| --- | --- |
| **green** | Openly licensed. Distill with attribution; informational images may be mirrored into `assets/`. |
| **amber** | Free to read, all rights reserved. Distill in your own words, link the source, never quote, never mirror images. |
| **red** | The content is the product its publisher sells. Not ingested at all; `discover.py` refuses to touch it. |

Sources at `mode: roadmap` stay in `sources.json` precisely so the exclusion is recorded in
code rather than remembered. See the roadmap in the root README for the permission plan.

## How updates affect existing content

**Additive by default.** A new item becomes a new entry appended to one theme file. Existing
entries are immutable: each is pinned to its own source, and nothing rewrites them.
`refresh_meta.py` then bumps the counts and coverage to match.

**Supersession is a human call.** When a source revises a framework, do not overwrite the old
entry. Add the new one and cross-reference the old as superseded. The pipeline surfaces
candidates; it never edits curated prose on its own.

## Files

| File | What it does |
| --- | --- |
| `sources.json` | Declarative registry: every source, its mode, license tier, theme and discovery strategy |
| `skill_lib.py` | Parses `references/` - covered URLs, counts, coverage, slugs. Run it bare for a status report |
| `extract.py` | Stdlib fetch plus HTML-to-markdown, with index and RSS helpers |
| `discover.py` | Lists source items not yet in the skill |
| `update.py` | Fetches them and stages a distillation prompt for each |
| `refresh_meta.py` | Recomputes every number and patches README + SKILL |
| `prompts/distill.md` | The canonical distillation spec, the single source of truth for entry shape |
| `staging/` | Gitignored working area |

## Adding a source

Append an object to `sources.json`. The fields that matter are `mode` (`watch`, `seed` or
`roadmap`), `license`, `theme` (which `references/<theme>.md` its entries land in),
`discovery` (`html-index`, `rss` or `single`) and `item_pattern`, a regex matched against the
**path** of each link on the index page. Then:

```bash
python3 pipeline/discover.py --source <your-id>   # check the pattern catches the right links
python3 pipeline/update.py  --source <your-id> --limit 1   # stage one and read the prompt
```

If the theme is new, create `references/<theme>.md` with an `# H1`, a `<!-- covers: ... -->`
line and an `<!-- order: ... -->` line. `refresh_meta.py` picks it up from there.

## Note on network

`discover.py` and `update.py` are the only parts that need network access. `skill_lib.py` and
`refresh_meta.py` are fully offline, which is why the counts can be trusted anywhere.
