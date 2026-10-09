---
id: ADR-0002
type: decision
updated: '2026-10-09'
status: proposed
---
# ADR-0002 — Memory implementation conventions

## Decision proposal

Use the repository root as the Obsidian vault, stable paths and IDs, root-relative
wikilinks, ISO date metadata, and a small Python validator using PyYAML 6.0.2.
Mirror phase state in the three essential notes and reject inconsistencies.
These conventions are implemented for Phase 0 review, not separately approved.

## Rationale

Root-level specifications remain navigable. A real safe YAML parser avoids
pretending that a regular-expression subset validates YAML. Explicit state fields
make common stale-handoff errors detectable without application infrastructure.

## Alternatives

A memory-folder-only vault would strand links to root specifications. A custom
YAML parser adds avoidable maintenance. Databases and full MARM are outside scope.

## Consequences

Validation needs the pinned dependency in [requirements-memory.txt](../../requirements-memory.txt).
PyYAML 6.0.2 was already available locally; no installation was performed.
The validator checks structure and basic state consistency, not whether a human
actually authorized a change or whether prose accurately represents evidence.
Human review remains necessary. Git files are prepared but no commit is created
automatically; normal review and commit workflow preserves their history.

Related: [[memory/DECISIONS]], [[memory/concepts/agent-memory]],
[[memory/decisions/ADR-0001-markdown-memory]].
