---
name: ahga-pull-request
description: Writes a pull request title and description from the branch changes, with the story number in the title. Use when the user asks to create, open or draft a pull request.
---

# Pull request

1. Find the base branch (usually the repository's default branch). Run `git log <base>..HEAD --oneline` and `git diff <base>...HEAD` to understand the whole branch, not just the last commit.
2. Find the story number. Look in the branch name, then in the commit messages. If it is not there, ask the user. Never invent one. If the user says there is no story, use the no-story variants below.
3. Write the title and the description using the formats below.
4. Show the title and the description to the user. Create the pull request, and push the branch if needed, only if the user asks you to.

## Title

```text
<STORY-ID> - <short description>
```

- `<STORY-ID>` is the story number exactly as written in the tracker (for example `PROJ-123`).
- `<short description>` is a brief summary of the change, with no final period.
- The whole title stays within 72 characters.

Example: `PROJ-123 - add password reset`

Without a story, the title is only the short description, with no prefix and no dash: `add password reset`.

## Description

Write the description in English, whatever the language of the commits or of the project. Use these sections, in this order. Drop a section only when it has nothing to say, except Summary and Changes, which are always present. Without a story, drop the Story section.

```markdown
## Summary

<One or two sentences: what this pull request does and why.>

## Story

<STORY-ID> - <link to the story, if known>

## Changes

- <Main change, grouped by theme rather than listed file by file.>
- <Another change.>

## Testing

- <How the change was verified: tests added or run, manual steps.>

## Notes

<Breaking changes, migrations, follow-ups, points where the reviewer should look closely, screenshots.>
```

Rules:

- Describe the intent and the effect of the change, not a copy of the diff.
- Keep it short: a reviewer should understand the pull request in under a minute.
- If you did not run the tests or could not verify something, say so in Testing instead of leaving it out.
