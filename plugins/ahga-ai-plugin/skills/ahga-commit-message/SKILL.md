---
name: ahga-commit-message
description: Writes a commit message from the staged changes. Use when the user asks for a commit message or wants their changes summarized for a commit.
---

# Commit message

1. Run `git diff --staged`. If nothing is staged, run `git diff` and say so.
2. Run `git log --oneline -10` to match the repository's language and style.
3. Decide whether the changes should be split into several commits (see "Splitting commits"). If so, propose one message per commit and say which files or hunks belong to each.
4. Propose a title of at most 72 characters, in the imperative mood, saying what the change brings.
5. Add a body only if the reason for the change is not obvious from the title.

## Splitting commits

Think about splitting before writing any message. A commit must hold one logical change.

- Split when the changes mix several types (for example a `feat` and a `fix`, or a `chore` alongside either), several scopes, or several unrelated purposes.
- Keep together the changes that only make sense together, such as a feature and its tests.
- Separate pure noise from real changes: formatting, renames and generated files go in their own `chore` commit.
- Order the commits so that each one leaves the project in a working state.
- If a file mixes several concerns, say which hunks go in which commit.
- If one title needs "and" to describe the change, it is probably two commits.

## Commit format

Every commit title must follow this format:

```text
<type>[(<scope>)]: <short description>
```

- `<type>` is one of `chore`, `feat` or `fix`, in lowercase. Use `feat` for a new feature, `fix` for a bug fix, and `chore` for anything else (maintenance, documentation, refactoring, configuration).
- `(<scope>)` is optional. Add it only when it makes the change clearer, for example the name of the agent or skill concerned (`feat(ahga-commit-message): ...`).
- `<short description>` is a brief summary, starting in lowercase, with no final period.
- The whole title stays within 72 characters.

Examples:

- `feat(ahga-add-component): add a checklist step`
- `fix: correct the frontmatter of an agent`
- `chore: update the README`

Propose the message without running `git commit`, unless the user asks you to.
