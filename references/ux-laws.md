# UX Laws

<!-- covers: cognitive laws of attention, memory, decision time and perception - Fitts, Hick, Miller, Jakob, Gestalt grouping, Doherty, Zeigarnik, peak-end -->
<!-- order: canonical -->

> The psychological laws that govern how people perceive, remember and decide inside an interface.
> Distilled from [Laws of UX](https://lawsofux.com/) by Jon Yablonski, which collects the underlying
> research. The laws themselves belong to the researchers named in each entry.
> Ordered alphabetically by the law each entry names, matching the source.

## Make it beautiful, then test it as if it were ugly
**Principle.** Visual polish raises how usable people believe an interface is, and that belief is sticky enough to mask real defects. Aesthetics buy tolerance for small friction, and they also buy silence in usability tests.
**Apply when.** Reviewing test results on a well-crafted prototype, or deciding how much visual quality to invest before validating a flow.
**The move.** Use the aesthetic-usability effect deliberately: polish to earn goodwill, but treat positive feedback on a beautiful prototype as unreliable. Probe for the problems users are excusing, watch behaviour rather than sentiment, and test the plain-but-correct variant to separate appeal from usability.
**Evidence.** Kurosu and Kashimura (1995) had 252 participants rate 26 ATM interface variants; perceived aesthetic appeal correlated more strongly with perceived ease of use than with actual usability.
**Source.** [Laws of UX - Aesthetic-Usability Effect](https://lawsofux.com/aesthetic-usability-effect/)

## Cut the option set before you improve the option copy
**Principle.** Past a modest number of options people do not choose better, they disengage. More choice reads as generosity to whoever built the menu and as work to whoever faces it.
**Apply when.** Pricing tables, plan pickers, category listings, settings screens, or any catalogue where users stall instead of selecting.
**The move.** Treat choice overload as the applied face of Hick's law: cut the set first, then structure what remains. Feature a recommended default, enable side-by-side comparison for options that genuinely need deliberation, and add search and filtering so the user narrows rather than scans.
**Anti-pattern.** Answering low conversion on a nine-tier pricing page by rewriting the tier descriptions.
**Source.** [Laws of UX - Choice Overload](https://lawsofux.com/choice-overload/)

## Group content into meaningful chunks, not even ones
**Principle.** People scan for relevance before they read for meaning. Information split into visually distinct, semantically coherent groups is absorbed far faster than the same information in a uniform block.
**Apply when.** Long forms, dense tables, settings pages, documentation, dashboards, phone numbers and reference codes.
**The move.** Chunk by meaning rather than by symmetry: group related fields, separate groups with real whitespace or a rule, and give each group a heading naming what it is for. The hierarchy between chunks matters as much as the chunks, because it tells the user which group to enter first.
**Evidence.** Rooted in George Miller's 1956 finding that short-term memory holds roughly seven units, where a unit can be a chunk rather than a single item.
**Source.** [Laws of UX - Chunking](https://lawsofux.com/chunking/)

## Assume the user is not evaluating your interface rationally
**Principle.** Judgment inside an interface runs on systematic shortcuts, not on evaluation. Users are not weighing your options; they are anchoring, defaulting, avoiding loss, and preferring whatever they saw first.
**Apply when.** Designing any comparison, default, price or moment of commitment, and whenever a research finding contradicts what users said they would do.
**The move.** Name the bias at work before designing with or against it: anchoring on the first price seen, status-quo bias on defaults, loss aversion at cancellation, confirmation bias in your own reading of research. Naming it turns a vague "users are irrational" into a specific, testable design decision.
**Anti-pattern.** Designing for an idealised rational user, then treating the gap between stated and actual behaviour as a research error.
**Source.** [Laws of UX - Cognitive Bias](https://lawsofux.com/cognitive-bias/)

## Spend the user's attention on the task, not on your interface
**Principle.** Every interface charges the user a mental fee. Intrinsic load is the irreducible difficulty of the task itself; extraneous load is everything the design added on top of it, and only the second is yours to cut.
**Apply when.** Any screen where users hesitate, re-read, or abandon without complaining.
**The move.** Separate the two loads before simplifying. Cut extraneous load first: decorative complexity, competing emphasis, jargon, layout that must be re-parsed on every visit. Manage intrinsic load by staging the task, carrying context forward, and never asking the user to hold something the system already knows.
**Evidence.** John Sweller's cognitive load theory, late 1980s, extending Miller's work on the roughly seven-item limit of working memory.
**Source.** [Laws of UX - Cognitive Load](https://lawsofux.com/cognitive-load/)

## Answer within 400ms or show that you are working
**Principle.** Interaction becomes productive when neither party waits on the other, and the practical boundary sits around 400 milliseconds. Below it attention stays on the task; above it the user's focus detaches and has to be re-acquired.
**Apply when.** Any interaction carrying a server round trip, a computation, or a transition: search, filtering, saving, navigation.
**The move.** Target sub-400ms actual response, and where you cannot reach it, buy the gap with perceived performance: optimistic UI, skeleton states, progress indication. A progress bar improves tolerance even when its accuracy is poor, and a deliberate short delay can raise perceived thoroughness for work users expect to be hard.
**Evidence.** Doherty and Thadani, IBM Systems Journal (1982), which established 400ms against the then-standard two seconds.
**Source.** [Laws of UX - Doherty Threshold](https://lawsofux.com/doherty-threshold/)

## Size and place targets by how hard they are to hit
**Principle.** The time to acquire a target falls as it grows and rises as it gets farther away, and small distant targets also raise the error rate. Pointing accuracy is a design variable, not a user attribute.
**Apply when.** Buttons, touch targets, menus, drag handles, close controls, and anything sized down to fit a layout.
**The move.** Apply Fitts's law: make the primary action the largest and nearest target, give targets enough spacing that a near-miss does not fire the wrong one, and exploit screen edges and corners, which behave as infinitely deep targets. On touch, size for the thumb's reach arc rather than for the design grid.
**Evidence.** Paul Fitts, 1954, established movement time as a function of target distance and size.
**Source.** [Laws of UX - Fitts's Law](https://lawsofux.com/fittss-law/)

## Match difficulty to skill, then get out of the way
**Principle.** Deep engagement appears in the narrow band where challenge matches ability. Too hard produces anxiety, too easy produces boredom, and both end the session.
**Apply when.** Onboarding, creative and editing tools, games, and any product where people work in long sessions.
**The move.** Design for flow: calibrate difficulty to the user's current skill rather than to the average, give immediate feedback so each action confirms itself, and remove the friction and delay that break concentration. Make advanced capability discoverable as skill grows instead of exposing all of it at once.
**Evidence.** Named by Mihaly Csikszentmihalyi in 1975.
**Source.** [Laws of UX - Flow](https://lawsofux.com/flow/)

## Show progress, and start it above zero
**Principle.** Motivation to finish rises with proximity to the goal, so effort accelerates near the end. It is the perception of progress that drives this, not the actual work remaining.
**Apply when.** Multi-step forms, onboarding checklists, profile completion, loyalty programmes, uploads.
**The move.** Apply the goal-gradient effect: always show a clear progress indicator, and grant artificial early progress so the user starts partway along rather than at nothing. Order the steps so the easiest come first, because early completions compound the effect.
**Evidence.** Clark Hull proposed the goal-gradient hypothesis in 1932 and showed in 1934 that rats ran progressively faster as they neared food.
**Source.** [Laws of UX - Goal-Gradient Effect](https://lawsofux.com/goal-gradient-effect/)

## Decision time rises with the number and complexity of choices
**Principle.** Every option added to a set lengthens the time to choose, and complexity within the options compounds it. The cost is paid in hesitation, which the user experiences as the product being hard.
**Apply when.** Navigation, menus, plan selection, settings, onboarding, and any moment where response time matters.
**The move.** Apply Hick's law: reduce the number of simultaneous options, break a complex decision into a sequence of smaller ones, and highlight a recommended path so the default carries the undecided. Use progressive onboarding to defer choices until they are relevant. Stop short of oversimplifying into abstraction, where the user can no longer tell the options apart.
**Evidence.** William Hick and Ray Hyman, 1952, on how the number of stimuli affects reaction time.
**Source.** [Laws of UX - Hick's Law](https://lawsofux.com/hicks-law/)

## Match the interface to the sites users already know
**Principle.** People spend nearly all their time on other products, so their expectations are formed elsewhere. Familiarity is not a lack of ambition; it is the budget you free up for the part of the product that is genuinely new.
**Apply when.** Choosing navigation patterns, form behaviour, icon meaning, or any moment where a novel interaction is being considered for its own sake.
**The move.** Apply Jakob's law: keep conventional patterns for conventional jobs and spend the novelty budget on your actual differentiator. When you must break a convention, let users fall back to the familiar version while they transfer their mental model.
**Anti-pattern.** Redesigning checkout or navigation to look distinctive, then paying for it in support tickets and abandoned carts.
**Source.** [Laws of UX - Jakob's Law](https://lawsofux.com/jakobs-law/)

## Draw a boundary to create a group
**Principle.** Elements inside a shared, clearly bounded area are perceived as belonging together, and the boundary overrides proximity: a border or background can group items that sit far apart, and can split items that sit close.
**Apply when.** Cards, panels, form sections, grouped list rows, toolbars, and anywhere spacing alone has failed to communicate structure.
**The move.** Use the Gestalt law of common region: enclose related elements in a shared container, background fill or border. Because it is the strongest grouping cue available, it is also the fastest way to imply a relationship that does not exist, so check that every container maps to a real group.
**Source.** [Laws of UX - Law of Common Region](https://lawsofux.com/law-of-common-region/)

## People will read the simplest interpretation available
**Principle.** Faced with something ambiguous or complex, perception resolves it into the simplest form that fits, because the simple reading costs least. Your layout will be understood as its simplest possible interpretation, not as its intended one.
**Apply when.** Complex layouts, iconography, data visualisation, illustration, and any composition that has to read at a glance.
**The move.** Apply the Gestalt law of Pragnanz: reduce forms to shapes that survive being simplified. Then test whether the intended structure is still the simplest available reading, because if a wrong grouping is simpler than the right one, that is the one users will take.
**Source.** [Laws of UX - Law of Pragnanz](https://lawsofux.com/law-of-pr%C3%A4gnanz/)

## Spacing is the cheapest grouping tool you have
**Principle.** Objects placed near one another are perceived as related, before any label, colour or border is read. Distance communicates relationship faster than anything you can write.
**Apply when.** Forms, above all the label-to-field distance, plus lists, toolbars, captions, and any layout using uniform spacing throughout.
**The move.** Use the Gestalt law of proximity: make the gap inside a group visibly smaller than the gap between groups. Uniform spacing is not neutral, it actively destroys structure. In a form, a label sitting closer to the next field than to its own is a defect, not a style choice.
**Anti-pattern.** Applying one spacing token everywhere, then adding borders to recover the grouping that even spacing removed.
**Source.** [Laws of UX - Law of Proximity](https://lawsofux.com/law-of-proximity/)

## Things that look alike are assumed to behave alike
**Principle.** Elements sharing colour, shape, size or orientation are perceived as one group with one function. Visual similarity is read as a promise about behaviour.
**Apply when.** Link and button styling, icon sets, tags and badges, repeated list items, and any design system carrying near-identical variants.
**The move.** Use the Gestalt law of similarity so that appearance follows function: everything that acts the same looks the same, and anything that acts differently looks different. The corollary matters more, because a non-interactive element styled like a link is a bug your users will find before you do.
**Source.** [Laws of UX - Law of Similarity](https://lawsofux.com/law-of-similarity/)

## Connect elements visually to state a relationship explicitly
**Principle.** Elements joined by a visible connector, whether a line, a shared bar or a continuous background, are perceived as more related than elements merely near or merely alike. Explicit connection is the strongest grouping signal available.
**Apply when.** Steppers and wizards, org and flow diagrams, timelines, grouped navigation, related-item rails.
**The move.** Apply uniform connectedness when a relationship must not be misread: draw the line between the steps rather than relying on their order, and use a shared surface to bind a header to the content it controls.
**Source.** [Laws of UX - Law of Uniform Connectedness](https://lawsofux.com/law-of-uniform-connectedness/)

## Design to the model the user already has
**Principle.** People arrive with a compressed model of how a system like yours works, built from everything similar they have used. Friction is the gap between that model and yours, and the user has no reason to close it.
**Apply when.** Naming, information architecture, novel interaction patterns, and any feature that tests well internally but confuses new users.
**The move.** Find the existing mental model before designing the new one, through interviews, card sorting and journey mapping, then match conventional patterns for conventional jobs such as cart, checkout and search. When you must diverge, do it in the one place that is your actual differentiator, and make the divergence visible rather than silent.
**Evidence.** Kenneth Craik proposed mental models in The Nature of Explanation, 1943.
**Source.** [Laws of UX - Mental Model](https://lawsofux.com/mental-model/)

## Chunk information rather than capping it at seven
**Principle.** Working memory holds roughly seven items, plus or minus two, but an item can be a chunk. The finding is about how information is grouped, not a licence to limit menus to seven entries.
**Apply when.** Anyone cites "seven plus or minus two" to justify a design constraint, and whenever information must be held in the head across steps.
**The move.** Apply Miller's law correctly: group content into meaningful chunks so each occupies a single slot, and remember that capacity varies with the user's prior knowledge and context. Where information must persist across steps, display it rather than requiring recall.
**Evidence.** George Miller, 1956, on the limits of immediate memory and absolute judgment.
**Anti-pattern.** Trimming a navigation menu to seven items and presenting it as a research-backed decision.
**Source.** [Laws of UX - Miller's Law](https://lawsofux.com/millers-law/)

## Prefer the design that survives having everything removable removed
**Principle.** Among solutions that work equally well, the one carrying the fewest assumptions and parts is the better one. Complexity avoided at the start is far cheaper than complexity removed later.
**Apply when.** Choosing between design directions, reviewing a feature that keeps growing, or auditing a screen that has accreted elements over time.
**The move.** Apply Occam's razor: strip elements until removing one more would break the function, and treat what remains as the design. Ask what each element assumes about the user, because the option carrying the fewest assumptions is usually the right one.
**Source.** [Laws of UX - Occam's Razor](https://lawsofux.com/occams-razor/)

## Nobody reads the manual, so put the help in the path
**Principle.** Users start using software immediately and skip the documentation, even when reading it would save them time overall. This is stable behaviour, not a failing to be corrected.
**Apply when.** Onboarding, complex tools, and any feature whose discoverability depends on a help-centre article.
**The move.** Accept the paradox of the active user and move guidance into the product: contextual tips at the moment of need, defaults that teach by example, empty states that demonstrate the first action, and inline explanation on every path a user might actually take. Documentation is a fallback, never the plan.
**Evidence.** Defined by Mary Beth Rosson and John Carroll, 1987.
**Source.** [Laws of UX - Paradox of the Active User](https://lawsofux.com/paradox-of-the-active-user/)

## Find the 20% of the product that carries the outcome
**Principle.** Effects distribute unevenly: a small share of causes produces most of the result. In a product, a minority of features, screens and users generate the majority of the value and of the problems.
**Apply when.** Prioritising a roadmap, allocating polish, deciding what to instrument, or triaging a long backlog.
**The move.** Apply the Pareto principle by measuring before assuming: identify the flows carrying the volume and the defects carrying the complaints, then concentrate effort there. The corollary is uncomfortable and useful, that most of what you maintain contributes little.
**Evidence.** Vilfredo Pareto observed that roughly 80% of Italy's land was held by 20% of its population.
**Source.** [Laws of UX - Pareto Principle](https://lawsofux.com/pareto-principle/)

## Set the expected duration, then beat it
**Principle.** A task expands to fill the time available for it. In an interface, the time a user expects a task to take becomes roughly the time it takes.
**Apply when.** Forms, checkout, onboarding, account setup, and any task where completion time is itself the friction.
**The move.** Apply Parkinson's law in both directions: constrain the expected duration by showing plainly how short the task is, then finish faster than promised. Autofill, saved payment details, smart defaults and pre-populated fields all shorten the actual time, and delivering under the stated expectation is what the user registers as fast.
**Source.** [Laws of UX - Parkinson's Law](https://lawsofux.com/parkinsons-law/)

## Design the peak and the ending, not the average
**Principle.** An experience is remembered by its most intense moment and its final moment, not by the sum of its parts. Improving the average changes the experience; improving the peak and the end changes the memory of it.
**Apply when.** Onboarding completion, purchase confirmation, cancellation, error recovery, waiting, and any journey you want remembered.
**The move.** Apply the peak-end rule: find the moment of maximum value and amplify it, then invest in the ending, which is usually the least designed screen in the flow. Weight negative peaks more heavily, since they are recalled far more vividly than positive ones of equal size.
**Evidence.** Kahneman and colleagues, 1993: participants preferred repeating a 90-second cold-water trial ending at a slightly warmer temperature over a 60-second one, despite more total discomfort.
**Source.** [Laws of UX - Peak-End Rule](https://lawsofux.com/peak-end-rule/)

## Accept whatever the user gives you, emit something strict
**Principle.** Postel's robustness principle, stated in RFC 761 (1980): be liberal in what you accept and conservative in what you send. Resilience comes from anticipating the range of what real people will do, then normalising it internally rather than rejecting it.
**Apply when.** Every input: phone numbers, dates, card numbers, addresses, search queries, pasted text, uploads.
**The move.** Apply Postel's law: accept variant input, translate it into the required form yourself, and show what you did. Strip the spaces out of the card number rather than erroring on them. Set boundaries where they genuinely exist and give clear feedback at those edges, but never make a user perform formatting that a parser can do.
**Anti-pattern.** A validation message rejecting input the system could have interpreted unambiguously.
**Source.** [Laws of UX - Postel's Law](https://lawsofux.com/postels-law/)

## Users see what serves their goal and nothing else
**Principle.** Attention filters the environment down to goal-relevant stimuli, so most of a screen is genuinely not perceived. Content is not seen because it is present; it is seen because it resembles the thing being looked for.
**Apply when.** Notices, banners, promotional content, state changes, and anything users report never having seen.
**The move.** Work with selective attention rather than against it. Avoid banner blindness by never styling real content like advertising, since ad-shaped things are filtered before they reach awareness. Guard against change blindness by not animating several regions at once, and by anchoring an important change where the user's attention already is.
**Source.** [Laws of UX - Selective Attention](https://lawsofux.com/selective-attention/)

## Put what matters at the ends of the list
**Principle.** What sits at the start and at the end of a series is recalled best; the middle is where things go to be forgotten. Position in a sequence is a memory decision, not a layout one.
**Apply when.** Navigation, toolbars, menus, feature lists, onboarding sequences, form field order.
**The move.** Apply the serial position effect: place the primary and most-used actions at the far left and far right of a navigation set, and park the least important items in the middle where lower recall costs nothing. In any ordered sequence, spend the first and last slots deliberately.
**Evidence.** Described by Hermann Ebbinghaus through the primacy and recency effects.
**Source.** [Laws of UX - Serial Position Effect](https://lawsofux.com/serial-position-effect/)

## Someone absorbs the irreducible complexity, so decide who
**Principle.** Every system carries a floor of complexity that cannot be designed away, only relocated. The only real question is whether the system carries it or the user does.
**Apply when.** Any simplification effort, and any feature where "let the user configure it" is being offered as the answer.
**The move.** Apply Tesler's law of conservation of complexity: name the irreducible part explicitly, then push it into the system through defaults, inference and automation. Design for how people actually behave rather than for an idealised rational actor, and support whatever complexity remains contextually, where it surfaces.
**Evidence.** Larry Tesler's framing at Xerox PARC: an engineer spending an extra week is cheaper than millions of users each spending an extra minute.
**Source.** [Laws of UX - Tesler's Law](https://lawsofux.com/teslers-law/)

## Make one thing different and it becomes the thing remembered
**Principle.** Among similar items, the one that differs is the one recalled and acted on. Emphasis is a scarce resource, and dividing it evenly spends it to no effect.
**Apply when.** Primary versus secondary actions, pricing tables, confirmation dialogs, and any layout where everything carries equal visual weight.
**The move.** Apply the Von Restorff effect: give the value-generating option visual dominance and demote the rest, for instance a ghost-styled Cancel beside a solid primary. Use emphasis sparingly, since competing highlights cancel each other out and over-styled elements get mistaken for advertising. Never carry the distinction on colour alone, and consider motion sensitivity if the contrast moves.
**Evidence.** Hedwig von Restorff, 1933, on improved recall for isolated items presented among similar ones.
**Source.** [Laws of UX - Von Restorff Effect](https://lawsofux.com/von-restorff-effect/)

## Show it rather than asking the user to hold it
**Principle.** Working memory holds and manipulates a small amount of information for a short time, and interruption wipes it. Anything a user must carry between screens is at risk, and the system usually knows it already.
**Apply when.** Multi-step flows, review and confirmation screens, comparisons, anything requiring a code from elsewhere, or an instruction that disappears before the action it describes.
**The move.** Reduce working-memory demand by keeping information visible where it is needed: carry entered values forward into review steps, keep comparison data on one screen, and never put an instruction on a screen the user must leave in order to follow it. Prefer recognition over recall wherever a choice can be shown instead of remembered.
**Source.** [Laws of UX - Working Memory](https://lawsofux.com/working-memory/)

## Incompleteness is what pulls people back
**Principle.** Unfinished tasks stay in mind more insistently than finished ones, so a visible open loop is itself a motivator. Completion releases the tension, and with it the pull.
**Apply when.** Onboarding checklists, profile completion, saved drafts, multi-session tasks, and content continuing below the fold.
**The move.** Apply the Zeigarnik effect: make incompleteness visible through checklists and progress indicators, and grant some progress up front so there is a loop to close. Use signifiers such as partially visible content to signal there is more, which turns a stopping point into a continuation.
**Evidence.** Bluma Zeigarnik, 1920s, found interrupted tasks were recalled more readily than completed ones.
**Source.** [Laws of UX - Zeigarnik Effect](https://lawsofux.com/zeigarnik-effect/)
