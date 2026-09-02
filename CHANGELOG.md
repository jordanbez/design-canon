# Changelog

All notable changes to the design-canon skill. Entries are additive by default: a new
source item becomes a new entry, and existing entries are immutable, each pinned to its
own source.

## 2026-09-02

No entries added. Pipeline and metadata corrections only.

- **Fixed** the `laws-of-ux` discovery pattern. It enumerated law-name suffixes, so it never
  matched `flow`, `chunking`, `peak-end-rule`, `paradox-of-the-active-user` or
  `law-of-pragnanz` - five of the thirty already in the skill. It now excludes site chrome
  instead, and reports 30 found / 0 new against the live index.
- **Fixed** the `principles-design-articles` pattern, which was returning `/articles/archive/`
  and `/articles/feed.xml` as if they were articles.
- **Added** `skill_lib.undiscoverable_entries()` and an assertion in `skill_lib.py`: every
  distilled URL must still be reachable by its own source's pattern. A pattern that is too
  tight fails silently as "nothing new", and the corpus is the only thing that can detect it.
- **Fixed** a `UnicodeEncodeError` that aborted `discover.py` on a Windows console whenever a
  candidate title carried a non-cp1252 character.
- **Corrected** the `humane-by-design-principles` note, which listed eight principles including
  two that do not exist (`reciprocal`, `thoughtful`) and omitted `transparent`. The site
  publishes seven, and all seven are distilled.
- **Fixed** the extractor dropping any link whose only content is an image. The Humane by
  Design garden is built from cover-image cards, so it reported 0 items indefinitely - an
  index that is broken and an index that is empty looked identical. It now falls back to the
  image's `alt` text and finds all six.
- **Added** `.gitattributes` pinning the repo to LF. `pipeline/sources.json` had been committed
  as CRLF, turning a three-line change into a 157-line diff.
- **Separated the skill from the tooling.** `npx skills add` was copying the whole repository
  into every installer's skills directory: 75 KB of maintainer tooling alongside 56 KB of
  actual skill, including `pipeline/prompts/distill.md`, a prompt spec written in the second
  person that an agent scanning the directory could read as instructions to itself. The skill
  now lives in `skills/design-canon/`, which the CLI resolves on its own, so the install
  command is unchanged and the pipeline stays maintainer-side. `LICENSE` is copied in beside
  it so attribution travels with the installed artefact.
- **Reviewed** all 49 entries for verbatim reuse by n-gram overlap against the fetched source
  pages, at a threshold of eight consecutive words. Four matched: two were reworded, one was
  a run of researchers' names, and the fourth is Postel's own sentence from RFC 761, now
  attributed to it rather than left reading as the site's prose.
- `SKILL.md` names the four recurring tensions between this canon and a commercial growth
  playbook (engagement against finitude, scarcity, defaults, friction with opposite
  beneficiaries), and instructs the agent to surface the trade-off rather than pick a side.
  Written for any companion library rather than a named one, since none is assumed installed.

## 2026-09-01

Initial release. 49 principles across 3 themes.

- **ux-laws** (30) - the full Laws of UX set: Fitts, Hick, Miller, Jakob, the five Gestalt
  grouping laws, Doherty threshold, Tesler, Postel, Occam, Pareto, Parkinson, peak-end,
  Zeigarnik, goal-gradient, serial position, Von Restorff, selective attention, working
  memory, cognitive load, chunking, choice overload, flow, mental model, aesthetic-usability
  effect, paradox of the active user.
- **usability-heuristics** (10) - Nielsen's ten, in his numbering.
- **humane-design** (9) - the seven Humane by Design principles plus both published essays.
- Pipeline: declarative source registry, offline delta detection, stdlib-only fetch and
  extract, staged distillation prompts, metadata sync.
- Weekly watch workflow over Humane by Design and principles.design.
