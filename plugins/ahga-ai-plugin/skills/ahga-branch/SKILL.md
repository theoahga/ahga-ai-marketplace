---
name: ahga-branch
description: Creates a git branch named <story>/<type>-<description>. Use when the user wants to create, start or name a branch for a story.
---

# Branch

Branch names follow this format:

```text
<story>/<type>-<description>
```

- `<story>` is the story number exactly as written in the tracker (for example `PROJ-123`).
- `<type>` is `chore`, `feat` or `fix`, with the same meaning as in the commit titles (see the `ahga-commit-message` skill).
- `<description>` is a short summary in lowercase kebab-case (letters, digits and hyphens only), a few words at most.

Example: `PROJ-123/feat-add-password-reset`

When the work has no story, drop the story and its slash: `<type>-<description>`, for example `feat-add-password-reset`.

## Steps

1. **Collect the inputs.** Ask the user for whichever is missing: the story number, the type and what the change is about. Never invent a story number. If the user says there is no story, use the no-story format. Infer the type from the request when it is obvious, and say which one you chose.
2. **Build the name.** Apply the format above. Translate the description to English kebab-case, without accents or special characters.
3. **Check for collisions.** List the existing local and remote branches. If the name exists, stop and ask the user.
4. **Pick the starting point.** Use the repository's default branch, up to date with the remote, unless the user names another base. If there are uncommitted changes, tell the user before switching branches.
5. **Create and switch to the branch.** Do not push it unless the user asks.
6. **Report.** Give the branch name and the base it was created from.
