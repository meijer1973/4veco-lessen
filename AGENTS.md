# 4veco-lessen Instructions

This repository is the student-facing lesson-material target. Do not treat it
as the place where production logic lives.

## Build Rule

Build, generate, validate, and refactor lesson materials through the companion
repository:

`C:\Projects\4veco\4veco-platform`

Use the platform repo's build scripts, validators, skills, references, and
workflow docs. In particular, read and follow:

- `4veco-platform/AGENTS.md`
- `4veco-platform/BUILD-PARAGRAPH.md`
- `4veco-platform/BUILD-CHAPTER.md`
- `4veco-platform/build-scripts/README.md`

## Do Not

- Do not invent new local build scripts in this repo when the platform has or
  should have the workflow.
- Do not hand-build generated outputs here as a one-off workaround.
- Do not edit machine-owned reference data from here.

## Allowed Here

Direct edits in this repo should be limited to lesson content or generated
artifacts when the platform workflow explicitly calls for writing them here.
If the task changes how materials are produced, make that change in
`4veco-platform` first.
