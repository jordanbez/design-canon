# Humane Design

<!-- covers: ethical and humane product design - attention, wellbeing, agency, dark patterns, inclusive and finite design -->
<!-- order: newest-first -->

> Guidance for designing products that respect people's attention, agency and wellbeing.
> Distilled from [Humane by Design](https://humanebydesign.com/) by Jon Yablonski.
> Dated essays sit at the top, newest first; the seven undated principles follow in the
> source's own order. This is one of the two watched sites, so new material lands here.

## Give the user the controls to the algorithm shaping their feed
**Principle.** Personalisation trades decision fatigue for agency. The same recommendation loop that removes the work of choosing also removes the ability to choose differently, and the loop is tuned for engagement rather than for the person's interest.
**Apply when.** Building recommendations, feeds, behaviour-derived defaults, or any system whose output narrows over time with use.
**The move.** Make the personalisation legible and steerable: expose usage awareness such as screen time and session counts, let the user tune or reset what the algorithm has inferred about them, and treat the recommendation model as a shared artefact they can edit rather than a black box acting on them.
**Evidence.** Netflix reported 92 billion hours watched in the first half of 2023; the essay also cites roughly 20% of streaming users abandoning a search when overwhelmed by options.
**Anti-pattern.** An infinite feed optimised for stickiness with no visible control over what it selects.
**Source.** [Humane by Design - 2024-01-23](https://humanebydesign.com/articles/the-cost-of-personalization/)

## Ask "and then what?" until you reach the people who never signed up
**Principle.** A product's consequences extend past its direct users to people who never chose it. Designing only for the happy path and the MVP externalises harm onto those indirect users, and it surfaces long after launch.
**Apply when.** Any feature involving routing, ranking, location, social feedback, or matching supply to demand at scale.
**The move.** Run three exercises before committing: second-order thinking, asking "and then what?" repeatedly to trace cascading effects; a futures wheel mapping direct and indirect consequences; and a premortem that assumes the project failed and works backwards to the cause. Widen the definition of good design to include effects on everyone affected, not only the user in the flow.
**Evidence.** Waze routing turning quiet streets into arterial traffic, AirTags repurposed for stalking, and the like button amplifying tribalism, all cited as consequences their designers never scoped.
**Source.** [Humane by Design - 2023-01-09](https://humanebydesign.com/articles/design-with-intentionality/)

## Design for the person your happy path excludes
**Principle.** Vulnerable users are harmed at exactly the edges a growth-optimised design ignores. Scale accelerates that harm, because a system tuned for the median case applies its assumptions to everyone.
**Apply when.** Anything social, anything carrying user-generated content, anything handling location or identity, and any roadmap justified purely by aggregate metrics.
**The move.** Design past the happy path: give people control over who can reach them and see their information, ship moderation and blocking tools rather than deferring them, and treat misuse cases as first-class requirements. Pair quantitative metrics with qualitative research, because aggregates hide the people being harmed.
**Anti-pattern.** Treating abuse handling as a post-launch trust-and-safety problem rather than a design requirement.
**Source.** [Humane by Design - Resilient](https://humanebydesign.com/principles/resilient/)

## Augment the person rather than capturing their attention
**Principle.** A humane product measures itself by the capability it adds to someone's life, not by the value it extracts from their attention. Those two goals diverge quickly, and the defaults reveal which one the product actually serves.
**Apply when.** Setting engagement metrics, designing algorithmic experiences, adding notifications, or shipping anything that makes automated decisions about a person.
**The move.** Hand control back: let people manage the algorithms shaping their experience, give real privacy and anonymity options, keep the technology invisible until needed rather than demanding presence, surface usage awareness so habits become visible, and keep a human in the loop wherever an automated decision affects someone.
**Anti-pattern.** Optimising for time-in-app and then reporting it as user value.
**Source.** [Humane by Design - Empowering](https://humanebydesign.com/principles/empowering/)

## Give the experience an ending
**Principle.** An experience without a natural stopping point removes the moment where a person would otherwise decide whether to continue. Bounding the experience is what converts consumption back into a choice.
**Apply when.** Feeds, video and audio players, recommendation rails, notification streams, anything paginated into infinity.
**The move.** Build the stopping points in: an explicit "you are all caught up" marker when the user reaches current content, a Load More control instead of automatic infinite scroll, and no autoplay without an intentional action. Each one restores a decision the interface had been making on the user's behalf.
**Anti-pattern.** A feed that auto-refills precisely so that no natural pause ever arrives.
**Source.** [Humane by Design - Finite](https://humanebydesign.com/principles/finite/)

## Design for disability first, then watch everyone benefit
**Principle.** Inclusive design starts from the whole spread of human ability rather than accommodating it afterwards. Solutions built for people with disabilities routinely turn out better for everyone.
**Apply when.** Any decision touching contrast, type size, motion, input method, or the platform's own accessibility settings.
**The move.** Start from the constraint rather than retrofitting to it: build teams with varied perspectives, design for disability first, and respect the platform features people already rely on, including zoom, contrast and font sizing. Give control over intrusive effects such as animation and infinite scroll instead of overriding the user's settings.
**Anti-pattern.** Disabling platform zoom or contrast in order to protect a layout.
**Source.** [Humane by Design - Inclusive](https://humanebydesign.com/principles/inclusive/)

## Add friction where a decision deserves one
**Principle.** Frictionless is a means, not a virtue. Some actions should be slightly harder, because the effort is what produces a considered choice instead of an accidental one.
**Apply when.** Irreversible actions, data sharing, financial commitments, publishing, and any default that enrols the user into something.
**The move.** Use positive friction deliberately: manual speed bumps such as confirmation at the point of real consequence, algorithmic speed bumps that slow unintended effects and deter bad actors, explicit opt-in rather than pre-checked defaults, and moderation tools letting people self-regulate their own consumption.
**Anti-pattern.** Accepting "reduce friction" as an unexamined goal, then auto-enrolling users into things they never chose.
**Source.** [Humane by Design - Intentional](https://humanebydesign.com/principles/intentional/)

## Match the interruption to the actual urgency
**Principle.** Attention is the resource a product spends most casually. Treating every message as equally urgent is not a notification strategy, it is the absence of one.
**Apply when.** Designing any notification, alert, badge, email or push, and any re-engagement mechanic.
**The move.** Grade delivery by real urgency and route each tier to a channel that matches it. Let people choose source, timing and channel separately rather than offering one global switch. Put the full content in the notification so it does not function as bait to open the app, and honour context, since the same message is welcome at one moment and an intrusion at another.
**Anti-pattern.** Truncated notifications written so the user has to open the app to find out what they said.
**Source.** [Humane by Design - Respectful](https://humanebydesign.com/principles/respectful/)

## State plainly what you collect, and make leaving as easy as joining
**Principle.** Transparency is the absence of misdirection, not the presence of a policy document. If the interface makes the consequential path harder to find than the profitable one, the design is deceptive regardless of what the terms disclose.
**Apply when.** Consent flows, account creation, data collection, subscription and cancellation, advertising placement.
**The move.** Give people a specific right to know what they are agreeing to, state what data is collected and why, provide real access to it and a working route to deletion. Avoid misdirection through consistent controls and a visible distinction between advertising and content. Make unsubscribing and account deletion as reachable as signing up, and collect on opt-in so the burden of justification sits with you.
**Anti-pattern.** Styling the option that serves the business as the obvious one and burying the user's.
**Source.** [Humane by Design - Transparent](https://humanebydesign.com/principles/transparent/)
