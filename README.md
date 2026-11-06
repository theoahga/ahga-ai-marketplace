# AHGA AI Plugin

A tool-agnostic collection of agents and skills, written as plain Markdown. It also ships as a Claude Code plugin marketplace (`ahga`).

## Contents

| Component | Type | Purpose |
| --- | --- | --- |
| `ahga-specbook` | Agent | Write, organize or review capability specifications in `spec/` |
| `ahga-commit-message` | Skill | Write a commit message from staged changes |
| `ahga-branch` | Skill | Create a branch named `<story>/<type>-<description>` |
| `ahga-pull-request` | Skill | Write a pull request title and description from branch changes |
| `ahga-add-component` | Skill | Add a new `ahga-*` agent or skill to this repository |

Every component is named `ahga-<name>`.

## Structure

```text
AGENTS.md                           Conventions for any AI assistant
plugins/
  ahga-ai-plugin/
    agents/ahga-<name>.md           Agents (name + description frontmatter)
    skills/ahga-<name>/SKILL.md     Skills (name + description frontmatter)
    .claude-plugin/plugin.json      Claude Code adapter
.claude-plugin/marketplace.json     Claude Code adapter
```

The agent and skill files use only `name` and `description` in their frontmatter and do not reference any specific assistant, so they can be reused as they are.

## Use with any tool

Copy or link the files from `plugins/ahga-ai-plugin/agents/` and `plugins/ahga-ai-plugin/skills/` into the location your tool reads agents or skills from. Check your tool's documentation for that location and for the frontmatter fields it accepts.

## Use with Claude Code

```text
/plugin marketplace add theoahga/ahga-ai-marketplace
/plugin install ahga-ai-plugin@ahga-ai-marketplace
```

To try it from a local clone, replace `theoahga/ahga-ai-marketplace` with the folder path. Components are then invoked as `ahga-ai-plugin:ahga-<name>`.

## Adding a component

Follow `plugins/ahga-ai-plugin/skills/ahga-add-component/SKILL.md`, or ask your assistant to use the `ahga-add-component` skill.

To validate the Claude Code adapter:

```bash
claude plugin validate .
```

Bump `version` in `plugins/ahga-ai-plugin/.claude-plugin/plugin.json` on every Claude Code release: users only receive an update when the version changes.
