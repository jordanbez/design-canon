# Design Canon - an Agent Skill

<!-- meta:badges -->
![Agent Skill](https://img.shields.io/badge/Agent-Skill-5b4ee6)
![Principles](https://img.shields.io/badge/principles-49-2ea44f)
![Themes](https://img.shields.io/badge/themes-3-2ea44f)
![Sources](https://img.shields.io/badge/sources-3-2ea44f)
![Updated](https://img.shields.io/badge/updated-2026--09--02-e67e22)
<!-- /meta:badges -->

> The public canon of interaction design - laws, usability heuristics and humane-design
> principles - distilled into short, applicable entries and packaged as an
> [Agent Skill](https://skills.sh) for Claude Code, Cursor, Codex, Copilot, Gemini and any
> skills.sh-compatible agent.

49 principles, each one linked back to the source it
was distilled from. It is also **self-maintaining**: a scheduled workflow watches the source
sites, detects material the skill does not cover yet, and opens a pull request with a
ready-to-run distillation prompt for each new item.

## Install

```bash
npx skills add jordanbez/design-canon
```

This pulls the skill into your agent's skills directory (`.claude/skills/`, `.agents/skills/`
and so on). Update later with `npx skills update design-canon`.

Or install it manually:

```bash
git clone https://github.com/jordanbez/design-canon.git ~/.claude/skills/design-canon
```

## What is inside

The skill loads only the theme relevant to your question, so a question about form spacing
never pulls in the notification guidance.

<!-- meta:themes -->
| Theme | Entries | Covers |
| --- | ---: | --- |
| [UX Laws](skills/design-canon/references/ux-laws.md) | 30 | cognitive laws of attention, memory, decision time and perception - Fitts, Hick, Miller, Jakob, Gestalt grouping, Doherty, Zeigarnik, peak-end |
| [Usability Heuristics](skills/design-canon/references/usability-heuristics.md) | 10 | Nielsen's 10 heuristics and heuristic evaluation - system status, error prevention, recognition over recall, user control |
| [Humane Design](skills/design-canon/references/humane-design.md) | 9 | ethical and humane product design - attention, wellbeing, agency, dark patterns, inclusive and finite design |
<!-- /meta:themes -->

Every entry uses one fixed shape - **Principle**, **Apply when**, **The move**, plus
**Evidence** and **Anti-pattern** where the source supports them, and always a **Source**
link - so an agent gets the named lever, the concrete action, and the proof.

The agent entry point is [`SKILL.md`](skills/design-canon/SKILL.md). Only
[`skills/design-canon/`](skills/design-canon/) is installed - the pipeline below stays in this
repository and never lands in your skills directory.

## Sources

<!-- meta:sources -->
- **Laws of UX** - 30 entries
- **Nielsen Norman Group** - 10 entries
- **Humane by Design** - 9 entries
<!-- /meta:sources -->

<!-- meta:coverage -->
Distilled entries span **2023-01-09 to 2024-01-23** where the source is dated; undated canonical references carry no date.
<!-- /meta:coverage -->

| Source                                                                             | Author        | Tier  | Treatment                            |
| ---------------------------------------------------------------------------------- | ------------- | ----- | ------------------------------------ |
| [Laws of UX](https://lawsofux.com/)                                                | Jon Yablonski | amber | distilled, never quoted              |
| [Nielsen Norman Group](https://www.nngroup.com/articles/ten-usability-heuristics/) | Jakob Nielsen | amber | distilled, never quoted              |
| [Humane by Design](https://humanebydesign.com/)                                    | Jon Yablonski | amber | distilled, never quoted, **watched** |
| [The Design Principles Collection](https://principles.design/)                     | Ben Brignell  | green | **watched**, not yet seeded          |
| [The Web Field Manual](https://webfieldmanual.com/design)                          | -             | amber | not yet seeded                       |
| [Lessons.design](https://lessons.design/)                                          | -             | amber | not yet seeded                       |

Tiers are declared in [`pipeline/sources.json`](pipeline/sources.json) and they govern what
the distiller may produce. **Green** means openly licensed. **Amber** means free to read but
all rights reserved, so the idea is restated in original words with a link back, never quoted
and never with images mirrored. **Red** means the content is the product its publisher sells,
and it is excluded from the corpus entirely.

## How it maintains itself

```
watch-sources.yml (weekly cron)
  -> discover.py    what is on the sites that the skill does not cover?
  -> update.py      fetch it, stage a distillation prompt per item
  -> pull request   you distill in Claude Code, review, merge
  -> refresh_meta.py  every number above recomputed from the content
```

The design borrows its central idea from
[heliocosta-dev/revenue-centric-design](https://github.com/heliocosta-dev/revenue-centric-design):
**the skill is its own manifest.** There is no state file recording what has been ingested.
Coverage, counts and delta detection are all derived from the `**Source.**` line at the bottom
of every entry, so the published numbers can never drift from the actual content, and delta
detection costs nothing.

Distillation is assisted, never autonomous. The workflow stages prompts; a human distills and
reviews every entry before it enters `references/`. See [`pipeline/README.md`](pipeline/README.md)
and [`AGENT.md`](AGENT.md).

## Roadmap

- [ ] **Seed the remaining three themes.** `writing-design-principles` and
      `principle-sets-catalog` from [principles.design](https://principles.design/), and
      `interface-craft` from The Web Field Manual and Lessons.design. Run
      `python3 pipeline/discover.py --seed` to see what is waiting.
- [ ] **Ask Growth.Design and Baymard for reuse permission.** Both publish case studies and
      e-commerce research that would make an excellent `case-studies` theme, and in both cases
      that research is the product they sell. They are recorded in `sources.json` as
      `mode: roadmap`, `license: red`, and are deliberately not ingested. The plan is to
      distill a sample in a private branch, write to each of them showing exactly what an entry
      would look like and how attribution works, and publish only on an explicit yes - the same
      route Helio took with @richardrx.
- [ ] **A `design-review` companion skill.** Today this skill is a library an agent reads.
      The next step is turning each principle into an assertable rule with an `id`, a
      `severity`, a `trigger`, a `check` and a `fix`, so an agent can audit a screen or a diff
      rather than only advise on it. [rams.ai](https://www.rams.ai/) proves the shape works,
      with 313 encoded rules scored 0 to 100 and delivered as a skill, an MCP server, a GitHub
      app and a CI action. The differentiator here would be openness and traceability: every
      rule citing the public research it comes from, rather than a closed proprietary ruleset.
- [ ] **Per-entry conflict notes.** Several principles genuinely oppose each other. Making
      those tensions explicit would make the skill more useful than any single source is.

## Contributing and takedowns

Corrections are welcome, especially on attribution and on evidence claims. If you are the
author of a source indexed here and want an entry changed or removed, open an issue and it
will be removed.

## License

The pipeline is MIT. The distilled entries are CC BY 4.0. The underlying ideas belong to their
original authors and are not this project's to license. See [LICENSE](LICENSE).
