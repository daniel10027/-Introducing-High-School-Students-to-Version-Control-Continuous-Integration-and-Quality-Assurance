# Reflection Report

## Challenges

The biggest early challenge with Git was building an accurate mental model
of the difference between the working directory, the staging area, and a
commit — `git status` became my most-used command just to keep track of
where my changes actually were. Branching felt safe once I understood that
a branch is just a movable pointer to a commit, but merge conflicts were
intimidating the first time: the `<<<<<<<`, `=======`, `>>>>>>>` markers
looked alarming until I realized they're just showing both versions side by
side so I can choose (or combine) the correct one. With CI, the hardest part
was YAML indentation — a single misaligned step silently breaks the whole
workflow file, and the error messages from GitHub Actions aren't always
obvious to a beginner. With QA, the trickiest part was writing tests that
actually exercised edge cases (like dividing by zero) rather than only the
"happy path."

## How CI streamlined development

Once the pipeline was in place, I no longer had to manually remember to run
tests and the linter before pushing — GitHub Actions did it automatically
and reported clear pass/fail status directly on each commit and pull
request. This caught a real lint issue (an unused variable and missing
type-hint spacing) before it could be merged, which gave me much more
confidence pushing changes without breaking the project for collaborators.

## How Git and QA improved collaboration and quality

Working in feature branches kept my in-progress work isolated from a stable
`master`, and resolving a genuine merge conflict taught me how two people's
changes can be reconciled without losing either person's work. The pull
request review cycle — receiving feedback to add a docstring, type hints,
and a missing zero-division guard — directly improved the final code and
showed how a second pair of eyes catches things the original author misses.
