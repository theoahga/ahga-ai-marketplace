# AGENTS.md

Tool-agnostic instructions for any AI coding assistant working in this repository.

## What this repository is

A collection of reusable agents and skills. The content is plain Markdown and does not depend on a specific tool. The `.claude-plugin/` manifests are only an adapter for Claude Code's plugin marketplace.

## Layout

```text
plugins/ahga-ai-plugin/
  agents/ahga-<name>.md           Agent: Markdown with name + description frontmatter
  skills/ahga-<name>/SKILL.md     Skill: Markdown with name + description frontmatter
  .claude-plugin/plugin.json      Claude Code adapter (ignore for other tools)
.claude-plugin/marketplace.json   Claude Code adapter (ignore for other tools)
```

## Conventions

- Every agent and every skill is named `ahga-<name>` (lowercase kebab-case). The `name` in the frontmatter equals the file name (agent) or folder name (skill).
- Frontmatter uses only `name` and `description`. Do not add tool-specific fields (for example tool allowlists, model selection or hooks) to the shared files.
- Instructions describe goals and steps in plain language. Do not reference a specific assistant, its tool names or its slash commands in the body of an agent or a skill.
- Write every file in this repository in English. A skill may tell the assistant to write its output in another language, such as the language of the project where it runs (for example, commit messages).
- Do not commit or push unless asked.

## Adding a component

Follow `plugins/ahga-ai-plugin/skills/ahga-add-component/SKILL.md`.
