# AGENT.md - design-canon

Read this first on any analysis of this project, and update it whenever the
structure changes.

## What this is

`design-canon` is a single **Agent Skill** distributed on GitHub and installed with
`npx skills add jordanbez/design-canon`. It distills the public canon of interaction
design - laws, usability heuristics, humane-design principles, and the craft of
writing design principles - into short, applicable entries an agent loads on demand.

It is also its own **generator**: a scheduled workflow watches the source sites,
detects material the skill does not cover yet, and stages a distillation prompt for
each. Distillation and review stay with a human.

## Layout

```
skills/design-canon/  THE ONLY THING THAT SHIPS. `npx skills add` installs this
                      directory and nothing else in the repo.
  SKILL.md            the agent entry point. Frontmatter + the routing table.
  references/*.md     the content. One file per theme. Each declares its own
                      ordering and coverage in its header.
  assets/             informational images. GREEN-tier sources only.
  LICENSE             travels with the skill so attribution reaches the installer.
pipeline/             maintainer tooling. NOT part of the installed skill.
  sources.json        declarative registry: every source, its mode and license tier
  skill_lib.py        parses references/ - counts, coverage, what is already covered
  extract.py          stdlib fetch + HTML to markdown
  discover.py         lists source items not yet in the skill
  update.py           fetches them and stages a distillation prompt for each
  refresh_meta.py     recomputes every number and patches README.md + SKILL.md
  prompts/distill.md  the canonical distillation spec (single source of truth)
  staging/            gitignored working area
.github/workflows/    watch-sources.yml, the weekly cron
```

## The one invariant

**The skill is its own manifest.** There is no state file listing what has been
ingested. Coverage, counts and delta detection are all derived from the
`**Source.**` line at the bottom of every entry in `references/*.md`. Never add a
parallel index; it would drift. If you change the shape of that line, change
`SOURCE_RE` in `pipeline/skill_lib.py` in the same commit.

## Rules that are not negotiable

1. **Nothing enters `references/` without human review.** The pipeline stages
   prompts; it never writes content.
2. **License tier governs the output.** Every source in `sources.json` carries a
   tier. AMBER means distill in your own words, never verbatim, never mirror
   images. RED means do not ingest at all.
3. **Every entry ends with a `**Source.**` link.** No exceptions - the tooling
   depends on it and attribution depends on it.
4. **Numbers are computed, never typed.** After editing `references/`, run
   `python3 pipeline/refresh_meta.py`.

## Common commands

```bash
python3 pipeline/skill_lib.py                    # what does the skill currently hold
python3 pipeline/discover.py                     # what is new on the watched sites
python3 pipeline/discover.py --seed              # what is missing from the bulk corpus
python3 pipeline/update.py --source laws-of-ux   # stage prompts for one source
python3 pipeline/refresh_meta.py --check         # preview the recomputed numbers
```

The pipeline is stdlib-only Python 3.10+. No `pip install` required.
