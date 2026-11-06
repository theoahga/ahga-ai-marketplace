---
name: ahga-specbook
description: Write, organize, or review authoritative capability specifications in spec/, including rules, invariants, acceptance and capability indexes. Use for capability specs or spec/ changes, not docs, implementation or test procedures alone.
---

# Specification

`spec/` owns authoritative required behavior and acceptance. `docs/` explains current behavior and practical use; link to the spec rather than duplicate normative rules. Report code/spec/docs discrepancies instead of presenting intended behavior as implemented.

## Files

Use one self-contained `spec/<area>/.../<capability>.md` per cohesive capability or cross-cutting concern. Default to one area level; subareas must group several related capabilities and improve navigation. Do not create a one-capability directory or mirror implementation structure. Split independent capabilities; keep shared context.

For multi-file specs, `spec/README.md` MUST provide product scope, shared terminology, and an area-grouped capability index with relative links. It supplies shared context, not a capability:

```markdown
# Specification

Short product purpose.

## Scope

- Owns ...
- Excludes ...

## Terminology

- **Term:** Meaning.

## Capabilities

### Area

- [Capability](area/capability.md): Short purpose.
```

Keep rules/capability details in their files, not duplicated in the index.

A capability file uses:

```markdown
# Capability name

Short purpose and scope.

## Rules

- **Rule name:** The system MUST ...
- **Another rule:** The system MUST NOT ...
- **Optional rule:** The system MAY ...

## Acceptance

- **Rule name:** Observable conditions and expected outcome.
- **Another rule:** Observable conditions and expected outcome.
- **Optional rule:** Observable conditions and expected outcome.
```

Require description, Rules, and Acceptance. Every rule MUST have acceptance coverage under the same short bold name. Put each normative rule in one capability's Rules; related files link rather than restate it. Other sections supply referenced supporting detail, not independent obligations.

Acceptance states initial conditions, trigger/input, and observable outcome that distinguish success/failure, not rule restatements or test implementation. Cover applicable boundaries, invalid inputs, failures, and recovery. Given/When/Then is optional. MAY rules cover both supported/enabled behavior and valid absent/disabled outcomes.

Other sections are optional; omit empty ones. Use MUST, MUST NOT, and MAY deliberately. Keep implementation, plans, and chronological decisions outside `spec/`. Tests or verification reference the capability path and rule name for acceptance coverage; they do not replace the spec's observable acceptance. No separate traceability document or numeric IDs are required.

## Section vocabulary

Prefer these names when they fit; add a clear name when none fits. Do not rename an existing concept without need.

- **Scope:** ownership, boundaries, exclusions.
- **Terminology:** capability-specific terms and meanings.
- **Rules:** required behavior and invariants.
- **Rationale:** reasons for current rules and tradeoffs.
- **Interface:** inputs, outputs, operations, contracts.
- **Data:** shapes, persistence, retention.
- **Configuration:** settings, defaults, precedence, overrides.
- **Limits:** size, time, capacity, resources.
- **Lifecycle:** states and transitions.
- **Errors:** failures, effects, recovery.
- **Security:** authority, trust boundaries, sensitive data.
- **Compatibility:** versions, migration, deprecation, backward compatibility.
- **Operations:** status, diagnostics, monitoring, maintenance.
- **Interactions:** related capabilities with relative links.
- **Examples:** non-normative illustrations.
- **Acceptance:** observable conditions and expected outcomes covering rules.

## Editing

- Read the whole capability and related files. Respect the requested scope and permissions; a review alone does not authorize edits.
- Ask one focused question if a material choice is unclear; do not invent the affected behavior while blocked.
- When editing is requested, replace obsolete behavior; update affected sections, capabilities, and index links within the authorized scope.
- Check stale, duplicate, conflicting, or out-of-scope text and broken links. Report changes or review findings, decisions, and unresolved gaps.
