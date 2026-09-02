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
Source label to use: `The Design Principles Collection - 2026-03-11`
License tier: **GREEN** - Openly licensed or explicitly permissive. Distill freely with attribution; informational assets may be mirrored into assets/.

---

# How Many Design Principles Should a Team Have? | Design Principles

- URL: https://principles.design/articles/how-many-design-principles
- Source name: The Design Principles Collection
- Published: 2026-03-11
- License tier: GREEN - Openly licensed or explicitly permissive. Distill freely with attribution; informational assets may be mirrored into assets/.

Some organisations publish long lists of design principles, while others use only a few. In practice, effective sets of principles tend to remain small.

---

# How Many Design Principles Should a Team Have?

[Ben Brignell](https://principles.design/about/ben-brignell/)

11 March 2026

There is no universal rule. But looking across many organisations, effective sets of principles tend to remain relatively small.

## How many principles are too many?

Some organisations publish ten or even fifteen design principles.

While these lists are usually well intentioned, long lists are difficult to remember and are unlikely to appear in everyday discussions.

Design principles are primarily a decision-making tool, but they can also play a broader role within an organisation. They can support cultural change, reinforce new ways of thinking, or help explain why a shift in approach is needed.

This was the case with the [GOV.UK Digital Service Standard](https://principles.design/examples/digital-service-standard). The list of principles is long, eighteen in total. But at the same time, the digital transformation work carried out by the GDS team affected every part of government. Principles were embedded into processes, clearly communicated and publicly visible.

In an environment shaped by risk, compliance and policy, questions about *why* change is necessary inevitably arise. In this context, principles helped explain the reasoning behind the transformation.

Was eighteen principles too many?

It depends on the context. The team understood how the principles guided decisions and the scale of the work they were supporting. For most organisations, however, a list of this size would be difficult to use in practice.

When the list becomes long, principles become harder to remember and less likely to influence everyday decisions.

Long lists often become documentation rather than tools. As the list grows, principles also tend to [drift closer towards being rules](https://principles.design/articles/difference-between-rules-and-principles) rather than guidance.

## Why small sets work better

Design principles are most useful when they can be remembered easily. Three, four or five principles are much easier to remember and use than eight, nine or ten.

A short set allows people to recall them quickly during discussions and apply them when evaluating different options.

When a principle can be referenced naturally in conversation, it becomes part of how a team reasons about design decisions.

For example, someone might ask:

>

“Are we over thinking this? Our principle is pragmatism…?”

Or someone else might say:

>

“This seems too rigid, it might conflict with our flexibility principle.”

In these moments, the principle is actively shaping the decision.

This is much harder to achieve when a team has a long list of principles that nobody can recall without looking them up.

## A common pattern

Looking across [many organisations](https://principles.design/examples/), effective sets of design principles often contain **between three and five principles**.

This number is not a strict rule, but it appears frequently.

A small set creates focus. It forces teams to identify the ideas that matter most when making decisions.

When too many principles exist, it becomes unclear which ones should take priority.

The longer the list gets the more diluted they can become.

## Principles are not meant to cover everything

One reason organisations sometimes produce long lists of principles is the desire to include every important idea. There is a natural tendency to lean towards [rule-making](https://principles.design/articles/difference-between-rules-and-principles) in order to feel safe, to feel like everything is covered, documented and in control.

But design principles are not intended to describe everything a team values. Gaps are healthy.

They are meant to guide decisions when there are multiple reasonable options.

Because of this, a small number of principles is often more useful than a comprehensive and well-documented list.

The goal is not completeness. The goal is clarity.

## In practice

Effective design principles are usually few in number and easy to recall.

They appear naturally in conversations and help teams explain why one option is better than another.

When a set of principles becomes too large to remember, its influence tends to fade.

In practice, the most useful sets are often the simplest: a small number of ideas that consistently guide how a team approaches design decisions.

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
