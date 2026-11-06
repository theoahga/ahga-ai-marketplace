---
name: ahga-add-component
description: Adds a new agent or skill to the ahga-ai-plugin plugin, enforcing the ahga- name prefix and tool-agnostic content. Use when the user wants to create, add or scaffold an agent or a skill in this plugin.
---

# Add an agent or a skill

Every agent and every skill in this plugin MUST be named `ahga-<name>`, and its content MUST stay tool-agnostic.

## Steps

1. **Determine the type and the name.** Ask the user for whichever is missing: agent or skill, and a short purpose. If they give a name, use it as `<name>`.
2. **Build the final name.**
   - Use lowercase kebab-case (letters, digits and hyphens only).
   - Prefix with `ahga-`. If the name already starts with `ahga-`, do not prefix it twice.
   - Example: `reviewer` becomes `ahga-reviewer`.
3. **Check for collisions.** Look in `plugins/ahga-ai-plugin/agents/` and `plugins/ahga-ai-plugin/skills/`. If the name exists, stop and ask the user.
4. **Create the file.**
   - Agent: `plugins/ahga-ai-plugin/agents/ahga-<name>.md`
   - Skill: `plugins/ahga-ai-plugin/skills/ahga-<name>/SKILL.md`

   The `name` in the frontmatter MUST equal the final prefixed name, and for a skill the folder name MUST match it.
5. **Write the frontmatter and body.** Use only `name` and `description` in the frontmatter, for both types:

   ```markdown
   ---
   name: ahga-<name>
   description: <what it does and when to use it>
   ---

   # <Title>

   <instructions>
   ```

   - Say in the `description` both what the component does and when to use it.
   - Describe goals and steps in plain language. Do not name a specific assistant, its tools or its slash commands in the body.
   - Do not add tool-specific frontmatter fields (tool allowlists, model, hooks, and so on).
   - Write everything in English.
6. **Update the README.** Add the new component to the `Contents` cell of the `ahga-ai-plugin` row in `README.md`.
7. **Check the plugin adapter, if available.** If the validation command listed in `README.md` can run here, run it from the repository root and fix any error. Otherwise skip this step.
8. **Report.** Give the user the created path. Mention that `version` in `plugins/ahga-ai-plugin/.claude-plugin/plugin.json` should be bumped before a new release of the plugin.

Do not commit or push unless the user asks.
