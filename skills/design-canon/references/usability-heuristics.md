# Usability Heuristics

<!-- covers: Nielsen's 10 heuristics and heuristic evaluation - system status, error prevention, recognition over recall, user control -->
<!-- order: canonical -->

> Jakob Nielsen's ten general principles for interaction design, first published in 1994 and still
> the most cited evaluation framework in the field. Distilled from the
> [Nielsen Norman Group's canonical article](https://www.nngroup.com/articles/ten-usability-heuristics/),
> last updated 30 January 2024. Kept in Nielsen's numbering.
> They are heuristics, deliberately broad rules of thumb, not rigid usability guidelines.

## Tell the user what is happening, immediately and in place
**Principle.** An interface must continuously report its own state, where the user is looking, within the time they expect. Trust is built from predictability, and predictability requires feedback on every action.
**Apply when.** Any action carrying a delay, any background process, any state that changed without the user causing it, any multi-step flow.
**The move.** Give feedback within a reasonable window (the Doherty threshold puts that near 400ms) and place it at the point of action rather than off in a corner. Communicate three things: that the action was received, what the system is doing now, and what state it ended in. Where the wait is long, show progress rather than mere activity.
**Anti-pattern.** A save that succeeds silently, so the user clicks again and creates a duplicate.
**Source.** [Nielsen Norman Group - 1. Visibility of system status](https://www.nngroup.com/articles/ten-usability-heuristics/)

## Speak the user's language, not the system's
**Principle.** Words, concepts and sequences should come from the user's world rather than from your database schema or internal team vocabulary. Terminology is an interface, and an unfamiliar term is a broken control.
**Apply when.** Naming features and states, writing error messages, ordering steps, choosing icons and metaphors.
**The move.** Take the vocabulary from research rather than from the backlog: interview users, read support tickets, use their nouns. Follow real-world conventions so information appears in a natural, expected order. When an internal term has leaked into the interface, the fix is renaming it, not attaching a tooltip.
**Anti-pattern.** Surfacing an internal status such as "provisioned", or a raw error code, in a message aimed at a customer.
**Source.** [Nielsen Norman Group - 2. Match between the system and the real world](https://www.nngroup.com/articles/ten-usability-heuristics/)

## Give every action a clearly marked way out
**Principle.** People trigger things by accident constantly. Recovery has to be a marked emergency exit rather than an extended process, or users stop exploring the product at all.
**Apply when.** Destructive actions, long forms, modal flows, bulk operations, anything irreversible.
**The move.** Prefer undo over confirmation: a confirmation dialog interrupts every user to guard against the rare mistake, while undo lets everyone move quickly and rescues the few who err. Where undo is impossible, mark the exit unambiguously, keep Cancel visible and plainly labelled, and never trap someone inside a flow they entered by accident.
**Anti-pattern.** A multi-step wizard whose only exit is the browser back button, which discards everything entered.
**Source.** [Nielsen Norman Group - 3. User control and freedom](https://www.nngroup.com/articles/ten-usability-heuristics/)

## Same word, same place, same behaviour
**Principle.** Users should never have to work out whether two different words, positions or behaviours mean the same thing. Consistency runs in two directions: internal, within your product, and external, with the conventions of the platform and the industry.
**Apply when.** Design system decisions, naming, the placement of recurring elements, and anywhere two teams have shipped the same concept twice.
**The move.** Enforce internal consistency so one concept carries one name and one appearance throughout, and honour external convention so learned behaviour transfers, which is Jakob's law in practice. Every deviation spends cognitive load, so make deviations deliberate and rare.
**Anti-pattern.** The same object called "workspace" in navigation, "project" in settings and "team" in billing.
**Source.** [Nielsen Norman Group - 4. Consistency and standards](https://www.nngroup.com/articles/ten-usability-heuristics/)

## Make the mistake impossible before you write the error message
**Principle.** A good error message is a repair; preventing the condition is the design. Errors split into slips, where the intention was right and the execution failed, and mistakes, where the intention itself was wrong, and the two are prevented differently.
**Apply when.** Destructive actions, free-text input the system could constrain, any form with a measurable error rate.
**The move.** Eliminate error-prone conditions first: constrain input to valid values, supply good defaults, and use helpful constraints and formatting rather than after-the-fact validation. Where the condition cannot be removed, confirm before commitment, but only on genuinely high-cost actions. Prevent slips with constraints; prevent mistakes with clearer information.
**Anti-pattern.** Accepting a wrongly formatted date, then explaining after submission what the format should have been.
**Source.** [Nielsen Norman Group - 5. Error prevention](https://www.nngroup.com/articles/ten-usability-heuristics/)

## Show the options instead of asking the user to remember them
**Principle.** Recognising something on screen is far cheaper than retrieving it from memory. Every piece of information a user must carry between screens is an avoidable charge against working memory.
**Apply when.** Search and filtering, multi-step flows, command interfaces, forms referencing data held elsewhere, anything with a syntax to learn.
**The move.** Make elements, actions and options visible, and keep whatever is needed to act either on screen or one glance away. Carry entered values forward, show recently used items, and state the required format inline rather than in help. Reserve recall for experts who have opted into it; never impose it on first-time users.
**Anti-pattern.** An empty search box with no suggestions, examples or recent queries, leaving the user to guess what is searchable.
**Source.** [Nielsen Norman Group - 6. Recognition rather than recall](https://www.nngroup.com/articles/ten-usability-heuristics/)

## Serve the novice and the expert with the same interface
**Principle.** Accelerators invisible to new users can serve experienced ones without adding surface. A product optimised only for first use punishes everyone who stays.
**Apply when.** Any product with repeat usage, high-frequency tasks, or a widening gap between new and power users.
**The move.** Layer the interface: keep the discoverable path primary, and place shortcuts, keyboard commands, gestures, bulk actions and saved configurations beneath it. Let users tailor the actions they repeat. The test is that removing every accelerator would leave the product still fully usable.
**Anti-pattern.** Forcing a power user through a five-step wizard they run twenty times a day.
**Source.** [Nielsen Norman Group - 7. Flexibility and efficiency of use](https://www.nngroup.com/articles/ten-usability-heuristics/)

## Every extra element steals visibility from the essential ones
**Principle.** This heuristic is about relevance, not visual sparseness. Content that is irrelevant or rarely needed competes with the content that matters and diminishes its relative visibility.
**Apply when.** Dense screens, dashboards, marketing pages, and any interface where a stakeholder has asked to add one more thing.
**The move.** Prioritise the content and features serving the primary goal, and remove or demote the rest rather than merely shrinking it. Judge each element by what it takes from its neighbours, not by whether it is useful in isolation. Fewer competing signals is the goal, which is entirely compatible with a rich, information-dense interface.
**Anti-pattern.** Reading the heuristic as a mandate for empty space and stripping out information users actually need.
**Source.** [Nielsen Norman Group - 8. Aesthetic and minimalist design](https://www.nngroup.com/articles/ten-usability-heuristics/)

## An error message names the problem and offers the way out
**Principle.** When prevention fails, the message must do three jobs: say plainly what happened, say precisely where, and offer a constructive way forward. A message doing fewer than three is an unfinished design.
**Apply when.** Validation, failed operations, empty results, permission denials, network failures.
**The move.** Write in plain language with no error codes, indicate the problem precisely rather than generically, and suggest a solution or a shortcut straight to it. Use conventional error styling so the message is found at all, and place it on the field or object that caused it. Preserve the user's work, because an error that discards input is two failures.
**Anti-pattern.** "Something went wrong", with no location, no cause and no next step.
**Source.** [Nielsen Norman Group - 9. Help users recognize, diagnose, and recover from errors](https://www.nngroup.com/articles/ten-usability-heuristics/)

## Ideally unnecessary, and when necessary, in context
**Principle.** The best outcome is a system needing no additional explanation, but complex tasks will still require documentation. Its usefulness depends entirely on being findable at the moment of need.
**Apply when.** Complex or infrequent tasks, configuration, integrations, and any feature generating repeat support questions.
**The move.** Present help in context, at the point where the task is performed, rather than as a separate destination. Make it searchable, list concrete steps rather than concepts, and keep it focused on the user's task rather than on your feature. Remember the paradox of the active user: documentation nobody will open is not a fix for a confusing flow.
**Anti-pattern.** Answering a recurring support question with a help article instead of repairing the interface that generates it.
**Source.** [Nielsen Norman Group - 10. Help and documentation](https://www.nngroup.com/articles/ten-usability-heuristics/)
