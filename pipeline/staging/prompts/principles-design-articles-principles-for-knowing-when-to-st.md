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

# Principles for Knowing When to Stop Designing | Design Principles

- URL: https://principles.design/articles/principles-for-when-to-stop-designing
- Source name: The Design Principles Collection
- Published: (no date on page - omit the date from the Source line)
- License tier: GREEN - Openly licensed or explicitly permissive. Distill freely with attribution; informational assets may be mirrored into assets/.

Knowing when to stop is as important as knowing where to start. These principles help designers recognise when a decision has been made and when further work...

---

# Principles for Knowing When to Stop Designing

[Ben Brignell](https://principles.design/about/ben-brignell/)

25 March 2026

At the moment the design world is obsessed with how fast things can be built. The conversations are about “I shipped a whole product in 2 hours” or “I built a startup in a weekend.”

New tools are creating faster workflows, quicker iterations, and the ability to produce more than ever before. In many ways, our new tools deliver and extend our capabilities as designers. But as always when the focus of conversation shifts to being about tools rather than outcomes, something has been lost in the process.

In music, knowing when to stop is just as important as knowing what to play. The pause gives structure to the sound. Without it, everything becomes noise.

As Mile Davis said “It’s not the notes you play, it’s the notes you don’t play.”

Tools will continuously improve and develop but they’re focused on delivery, shipping, iterations, not pausing or reflection.

These principles for knowing when to stop are not about slowing down for the sake of it. They’re about recognising when a decision has already been made, and when further work stops serving the user and starts serving the designer.

And ultimately understanding why we are building something rather than how quickly we are building something.

## 1. Stop when the next change is for you, not the user

Not every improvement is meaningful.

When changes are driven by taste, preference, or the desire to explore, are they solving a design problem? At this point, design becomes self-expression rather than problem solving. It’s art, not design.

This is often the quiet moment where good design work starts to drift.

## 2. Stop when the problem isn’t proven

Design without evidence is speculation.

Is the problem even real? If you can’t clearly point to a problem through research, behaviour, or observable friction you’re no longer solving something real. You’re designing in anticipation of a need that may not exist.

This doesn’t mean certainty is required, but it does mean intent should be grounded.

## 3. Stop when the question shifts from “why?” to “how?”

The moment the conversation becomes about execution, the decision is already behind you.

“How should this work?”, is not a design question. It’s a delivery question. The risk is that designers continue to iterate as if the core problem is still open, when in reality it has already been resolved.

Continuing to design at this point often leads to unnecessary variation rather than better outcomes.

## 4. Stop when you’re redesigning not refining

Refinement reduces uncertainty. Redesign introduces it.

Often we’re asked to help with a “redesign” but often we’re just building the same thing but different.

If each iteration creates new questions instead of resolving existing ones, the work is no longer converging. It’s diverging again, often without intention.

This is one of the clearest signals that we’ve crossed from improvement into reinvention.

## 5. Stop when the design can’t be tested in its current form

Test a design as early and in as fit a state as possible for who you’re testing it with. If it can’t be shown, used, or experienced by someone else, further iteration is disconnected from reality. The only meaningful next step is getting some feedback, not additional polish. The polish can go on forever.

Design only improves through contact with use.

## 6. Stop when you’re designing for edge cases

Edge cases are important but they shouldn’t lead. Discussions around edge cases can dominate meetings.

When rare scenarios begin to dictate core decisions, it’s often a sign that the central use case hasn’t been fully resolved. Designing for the margins before stabilising the centre creates fragile solutions and is often a very slow and painful journey.

Solve the common case well first. The edges can follow.

## 7. Stop to allow time to learn

Design doesn’t end when you stop working on it.

The most valuable insights come after pausing for feedback, testing or release, when real behaviour replaces assumptions. Without this pause, there’s no opportunity to understand whether you were close to getting things right.

Stopping isn’t the end of design. It’s a pause that makes learning possible.

You don’t need to stop for long. Stopping doesn’t slow things down. But knowing when to stop is what turns design from activity into decision-making.

I write occasionally about how principles function in real organisations, where they succeed, where they fail, and how they evolve over time.

If that’s useful to you, you can subscribe below.

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
