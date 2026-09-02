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
Source label to use: `The Design Principles Collection - 2026-03-06`
License tier: **GREEN** - Openly licensed or explicitly permissive. Distill freely with attribution; informational assets may be mirrored into assets/.

---

# Why Most Design Principles Fail | Design Principles

- URL: https://principles.design/articles/why-most-design-principles-fail
- Source name: The Design Principles Collection
- Published: 2026-03-06
- License tier: GREEN - Openly licensed or explicitly permissive. Distill freely with attribution; informational assets may be mirrored into assets/.

Many design principles are really statements of values. Values describe what a team believes. Principles guide decisions. Values express intent. Principles h...

---

# Why Most Design Principles Fail

[Ben Brignell](https://principles.design/about/ben-brignell/)

6 March 2026

Many organisations publish design principles. They appear in slide decks, design systems and internal documentation. They are sometimes printed on posters and hung on office walls. Yet they are rarely used.

Meetings still go on and on. Teams argue over the same questions. Decisions often depend on opinion or whoever speaks the loudest.

The problem is usually not that teams lack design principles. The problem is that most design principles don’t work.

## They are written like slogans

Many design principles sound impressive, they’re idealistic and make everyone feel positive. They come from great motives.

*Be user-centric.*
*Keep things simple.*
*Delight the customer.*

But these are not really principles. They are aspirations. They describe how a team would like their work to feel.

A design principle should do something more practical. It should help a team make a decision when there are several possible options.

A **slogan** describes *intent*. A **principle** guides a *choice*.

For example:

>

“Keep things simple.”

What does that mean in practice?

“Simple” is subjective.

Simple for whom?
Simple compared to what?
Simple in which situation?

“Simple” sounds sensible, but it’s also very vague. Different people will interpret simple in completely different ways.

One designer might think simple means removing options. Another might think it means reducing visual clutter. Someone else might think it means hiding complex features behind a menu so the initial view is clean.

All of those interpretations could be defended as “keeping things simple”.

There is another problem here. Simplicity is not always the right goal.

Imagine applying the same idea of keeping things simple when designing an aircraft cockpit. A cockpit would certainly be simpler if it contained only a steering wheel and a start button. But that level of simplicity would make it completely unusable for its purpose.

A cockpit contains many instruments and controls because the pilot needs them. Removing them might make the interface look simpler, but it would make the aircraft much harder — and far more dangerous — to operate.

So the instruction “keep things simple” does not really guide a decision. It only describes a general preference.

A principle needs to go a step further. It needs to explain what should happen when things become complicated.

A more useful principle might be something like:

>

“Prefer what matters.”

Now a team has something they can use. If a design includes too much information, the principle guides them towards what to prioritise. The discussion becomes about prioritisation rather than personal preference. The discussion becomes about what truly *matters*.

## They avoid trade-offs

Real principles reveal priorities. Many sets of principles list ideas that sound sensible but never conflict with one another.

A typical list might look like this:

*Be consistent*
*Be flexible*
*Be simple*
*Be powerful*

All of these sound reasonable. But none of them help when a decision becomes difficult. Real design work involves trade-offs.

Sometimes consistency conflicts with clarity. Sometimes simplicity conflicts with flexibility.

A useful principle helps resolve those moments. If everything is equally important, nothing actually guides the decision.

## There are too many of them

Some organisations publish ten or fifteen design principles. Long lists are difficult to remember and difficult to recall in conversations when discussing a decision. When principles become long lists, they turn into documentation instead of tools. A small number of principles is easier to remember and easier to use in conversation.

Good principles should appear naturally in discussions:

“Does this follow our clarity principle?”

“This might conflict with our accessibility requirement.”

“Does this feature really matter here?”

If nobody can remember them, they will never influence decisions. The most effective examples use 3-5 principles.

## They are never used

The real test of a design principle is very simple. Does anyone actually refer to it?

If principles only exist on a website or inside documentation, they are unlikely to matter.

When principles work well they become part of everyday language. Teams refer to them during discussions and use them to justify decisions. They help people explain and understand why one option is better than another. Without that practical use, they remain decorative.

## They are often confused with values

Many design principles are actually organisational values. Design principles aren’t mission statements.

**Values** describe what a company *believes*.

**Principles** guide how teams make *decisions*.

Both are important, but they serve different purposes.

A value might say:

>

We value transparency.

A principle might say:

>

Help the user understand what is happening and why.

**Values** shape *culture*.

**Principles** shape *decisions*.

When the two are mixed together, principles become vague and difficult to apply.

## What principles are really for

Design principles are not statements of intent. They are tools. They help teams make decisions when things are unclear. They reduce debate. They give people a shared way to reason about choices.

When written well, they quietly shape how work gets done. When written poorly, they become slogans that nobody uses.

The difference is not whether a team has principles. It is whether those principles actually guide decisions.

Often design principles are confused with rules. It’s important to understand the difference between principles and rules. This distinction is explained in the free sample chapter of the field guide [Design Principles in Practice](https://principles.design/samples/design-principles-in-practice/).

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
