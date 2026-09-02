# Distillation spec - how to turn a source item into a design-canon entry

You are distilling ONE item from a monitored design source into ONE reusable entry for
the **design-canon** agent skill. The skill is in **ENGLISH**; translate faithfully if the
source is not. You are writing for an AI agent that will apply this while advising on a
real interface, so every entry must be actionable, not encyclopedic.

## Output format (use EXACTLY this shape)

```
## <short imperative title - the instruction, not the noun>
**Principle.** <1-3 sentences: the reusable heuristic, generalised. State the mechanism, not the anecdote.>
**Apply when.** <the concrete trigger or situation where this decides something.>
**The move.** <the concrete action. KEEP every NAMED mechanism - Fitts's law, Von Restorff effect, Doherty threshold, Zeigarnik effect, recognition over recall, Tesler's law of conservation of complexity. Naming the lever is most of the value.>
**Evidence.** <ONE tight line, ONLY if the source cites a study, statistic, or named case. Otherwise omit the line entirely.>
**Anti-pattern.** <ONE line naming the concrete failure this prevents, ONLY if the source identifies one. Otherwise omit.>
**Source.** [<Source name> - <YYYY-MM-DD>](<url>)
```

The `**Source.**` line is load-bearing. `skill_lib.py` parses it to compute coverage,
counts and what is already ingested, so it must be the last line of every entry and must
match that shape exactly. Include the date only when the source page is actually dated;
for undated canonical pages use a distinguishing sub-label instead:
`**Source.** [Laws of UX - Jakob's Law](https://lawsofux.com/jakobs-law/)`

## Rules

- **Principle only, never verbatim.** Reproduce the idea in your own words. Do not paste the
  source's sentences, even one good one. If a phrase is genuinely unimprovable, the entry is
  wrong: restate the mechanism instead.
- **60-110 words per entry.** An entry longer than that is an article, not a principle.
- **One theme per entry.** Route it to exactly one `references/<theme>.md`.
- **Preserve named mechanisms.** The law, bias, heuristic or framework name is the payload.
  An entry that describes an effect without naming it has thrown away its value.
- **Be honest about evidence.** If the source claims a number, keep the number and its source.
  If it does not, omit `**Evidence.**` rather than inventing plausibility.
- **No hedging prose.** "It is important to consider" is not a move. Write the imperative.
- **Do not duplicate.** Check the target theme file first; if the principle is already there
  from another source, strengthen the existing entry instead of adding a near-twin.

## License tiers (this governs what you may write)

Every staged item is tagged with a tier. It is not advisory.

| Tier | What you may produce |
| --- | --- |
| **GREEN** | Openly licensed. Distill freely with attribution. Informational images may be mirrored into `assets/` and referenced as `../assets/<file>`. |
| **AMBER** | Free to read, all rights reserved. Distill the idea in your own words and link the source. **Never** reproduce the original prose, **never** mirror images. |
| **RED** | The content is the product its publisher sells. **Do not distill it at all.** It should not have reached you; stop and report it. |

Attribution is not optional at any tier. Every entry carries its `**Source.**` link back to
the original, and the README credits each source by name.

## Ordering inside a theme file

Each theme file declares its own ordering in its header:

- `<!-- order: newest-first -->` - dated material (articles, essays). Newest entry at the top.
- `<!-- order: canonical -->` - undated canon with a natural sequence (the 10 heuristics in
  Nielsen's numbering, the laws alphabetically). Keep the declared sequence.

## Theme routing

| slug | covers |
| --- | --- |
| `ux-laws` | cognitive laws of attention, memory, decision time and perception - Fitts, Hick, Miller, Jakob, Gestalt grouping, Doherty, Zeigarnik, peak-end |
| `usability-heuristics` | Nielsen's 10 heuristics and heuristic evaluation: system status, error prevention, recognition over recall, user control |
| `humane-design` | ethical and humane product design: attention, wellbeing, agency, dark patterns, inclusive and finite design |
| `writing-design-principles` | how to write, apply, test and evolve a set of design principles that actually changes decisions |
| `principle-sets-catalog` | real principle sets published by organisations, as worked examples of the craft |
| `interface-craft` | hands-on interface and web craft: layout, forms, states, typography, performance as UX |

## Worked example (the bar to hit)

```
## Match the interface to the site users already know
**Principle.** People spend nearly all their time on other products, so their expectations are formed elsewhere. Familiarity is not a lack of ambition; it is the budget you free up for the part of the product that is genuinely new.
**Apply when.** Choosing navigation patterns, form behaviour, icon meaning, or any moment where a novel interaction is being considered for its own sake.
**The move.** Apply Jakob's law: keep conventional patterns for conventional jobs and spend the novelty budget on your actual differentiator. When you must break a convention, let users fall back to the familiar version while they transfer their mental model.
**Anti-pattern.** Redesigning checkout or navigation to look distinctive, then paying for it in support tickets and abandoned carts.
**Source.** [Laws of UX - Jakob's Law](https://lawsofux.com/jakobs-law/)
```

## Before you hand anything back

State, for each entry: the target `references/<theme>.md`, the entry itself, and where in the
file it goes given that file's declared ordering. Then **wait for the maintainer's OK**. Nothing
enters `references/` without a human reading it first - that review is the entire quality gate.


---

# ITEM TO DISTILL

Target file: `references/writing-design-principles.md`
Source label to use: `The Design Principles Collection`
License tier: **GREEN** - Openly licensed or explicitly permissive. Distill freely with attribution; informational assets may be mirrored into assets/.

---

# The Difference Between Rules and Principles | Design Principles

- URL: https://principles.design/articles/difference-between-rules-and-principles
- Source name: The Design Principles Collection
- Published: (no date on page - omit the date from the Source line)
- License tier: GREEN - Openly licensed or explicitly permissive. Distill freely with attribution; informational assets may be mirrored into assets/.

Understanding how principles help with decision making starts with understanding how they differ from rules. Rules remove choice, principles guide choice.

---

# The Difference Between Rules and Principles

[Ben Brignell](https://principles.design/about/ben-brignell/)

11 March 2026

Understanding how principles help with decision making starts with understanding how they differ from rules. The distinction matters. Rules and principles serve very different purposes. Yet many “design principles” are written more like rules.

## What rules do

Rules remove ambiguity. Rules are rigid. They tell people exactly what must happen. Rules usually lead to a consequence, either:

1. the rule is broken, or
1. something happens when the rule isn’t followed.

For example:

>

**Our logo must always appear on a white background.**

This rule guarantees consistency. Everyone knows exactly what to do.

A rule like this prevents designers from using the logo on:

- coloured backgrounds
- photography
- illustrations
- gradients

Even if those options might work perfectly well.

Rules assume there is one correct answer or only one solution has been considered.

In many situations, especially technical or legal ones where a level of compliance has to be reached, rules are appropriate.

## What principles do

Principles work differently.

Instead of prescribing a single outcome, they describe what a good outcome should achieve.

Consider the same example written as a principle:

>

**The logo should be clearly legible.**

The goal is the same: protecting the visibility of the logo. But now designers have room to explore solutions.

They can place the logo on different backgrounds, colours or images, as long as the logo remains easy to see.

The principle does not dictate the design.

It guides judgement.

## Why this matters

Design decisions are rarely as simple as deciding how to display a logo. Design rarely involves a single correct answer. Most design work involves balancing competing priorities between different people and different goals, navigating budgets, timelines, and politics.

For example:

- clarity vs completeness
- consistency vs flexibility
- simplicity vs capability

Rules struggle in these situations because they assume the answer is fixed.

Principles acknowledge that design decisions often involve tension between competing forces.

They help teams navigate those trade-offs.

## Visualising how principles work

One way to think about this is to imagine a design decision being shaped by different priorities pulling in different directions. Principles help teams balance those forces and arrive at a thoughtful outcome.

This idea is illustrated in the sample chapter of [*Design Principles in Practice*](https://principles.design/field-guide/), where the relationship between design decisions and principles is explored in more detail.

→ **[View the sample chapter](https://principles.design/samples/design-principles-in-practice/)**

## Rules and principles both have their place

Most organisations need both. Rules are useful when consistency or compliance is essential. Principles are useful when teams need guidance to make thoughtful decisions.

Rules define the answer.

Principles help teams find the best answer.

Or more simply:

**Rules remove choice.** **Principles guide choice.**

If you’re interested in how design principles help teams make better decisions, I occasionally share new articles and ideas by email.

You can sign up below.

No spam. Unsubscribe any time.
See our [Privacy Policy](https://principles.design/privacy/).

Written by [Ben Brignell](https://principles.design/about/ben-brignell/)

### Practical guidance for
better design decisions

Sign up for occasional guidance, examples, and updates on using design principles in practice.

No spam. Unsubscribe any time.
See our [Privacy Policy](https://principles.design/privacy/).

principles.design is created and curated by [Ben Brignell](https://principles.design/about/ben-brignell/).

### About Ben

A product strategist and UX consultant with 25 years helping teams make better decisions.

[Learn more →](https://principles.design/about/ben-brignell/)

### Clarity for complex product organisations

Ben advises product and engineering leaders on decision-making, alignment and turning principles into practice.

[Discuss an engagement →](https://principles.design/consulting/)

Know a set of design principles that could be included? [Submit an example](https://principles.design/contribute/).

[Consulting](https://principles.design/consulting/) · [Try the audit](https://principles.design/audit/) · [Newsletter](https://principles.design/newsletter/)

[About](https://principles.design/about/) · [Browse principles](https://principles.design/browse/) · [Contact](https://principles.design/contact/)

[Access your purchases](https://principles.design/access-purchases/)

[Privacy Policy](https://principles.design/privacy/)

View the [design system](https://principles.design/design-system/) for this site.

© [Brignell Ltd](https://brignell.uk) — Registered in England and Wales, Company No. 9282895
