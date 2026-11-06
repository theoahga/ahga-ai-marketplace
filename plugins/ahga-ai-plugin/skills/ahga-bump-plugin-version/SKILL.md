---
name: ahga-bump-plugin-version
description: Increments the version of the ahga-ai-plugin plugin for a pull request, once per branch, choosing major, minor or patch from the changes. Use when the user wants to bump, increment or update the plugin version, or when a pull request is about to be created or updated in this repository.
---

# Bump the plugin version for a pull request

The version of the plugin lives in `plugins/ahga-ai-plugin/.claude-plugin/plugin.json`. Users only receive an update when that version changes, so every pull request MUST bump it exactly once.

## Steps

1. **Read the current version.** Open `plugins/ahga-ai-plugin/.claude-plugin/plugin.json` and read the `version` field. It MUST follow `MAJOR.MINOR.PATCH` (digits only, for example `0.1.0`). If it does not, stop and ask the user.
2. **Check whether this branch already bumped the version.** Find the main branch (`main` unless the repository says otherwise). Read the same field from that branch with `git show main:plugins/ahga-ai-plugin/.claude-plugin/plugin.json`.
   - If the value differs from the current one, the branch has already bumped the version. Do not bump again. Report the existing values and stop.
   - If the value is the same, continue.
3. **Choose the increment from the changes.** Read the commit subjects and bodies of the branch (`git log main..HEAD`), and the uncommitted changes if there are any. Use the highest level that applies:
   - **major**: a breaking change, marked by `!` after the type (for example `feat!:`) or by a `BREAKING CHANGE:` footer. Reset minor and patch to `0`.
   - **minor**: a new agent or skill, or a `feat:` commit. Reset patch to `0`.
   - **patch**: anything else, such as fixes, documentation or refactoring.
   If the changes do not make the level clear, use patch and say so in the report.
4. **Write the new version.** Change only the `version` value in `plugin.json`, keeping the file's formatting. Do not change `marketplace.json`, which has no version field.
5. **Check the file.** Confirm that the file is still valid JSON and that `version` holds the new value.
6. **Report.** Give the old and new versions, the increment chosen and why. Remind the user that the change must be part of the pull request's commit. Do not commit or push unless the user asks.

Write everything in English, except the report, which follows the user's language.
