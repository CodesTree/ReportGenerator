---
id: ADR-0001
type: decision
updated: '2026-10-09'
status: approved
approval_ref: memory/sessions/2026-10-09-phase-0.md
---
# ADR-0001 — Markdown memory foundation

## Decision and authority

Prompt 2 explicitly mandates Git-versioned Markdown, YAML frontmatter,
Obsidian-compatible wikilinks, lightweight Python validation, selective retrieval,
consolidation, session handoffs, and mandatory end-of-task synchronization.
This status records a user mandate, not approval of completed Phase 0 deliverables.
Authorization evidence: [[memory/sessions/2026-10-09-phase-0]].

## Rationale

Persistent, readable repository records preserve decisions and context across
sessions while matching the project's lightweight engineering constraint.

## Alternatives

Chat-only context lacks persistent handoffs. Full MARM and database-backed memory
are excluded by the user in Phase 0. Neither is installed or evaluated as an
application technology choice.

## Consequences

Agents must maintain and validate notes. Graph relationships are explicit links;
retrieval and consolidation are agent responsibilities rather than background
services. No SQLite, vectors, embeddings, MCP server, or code indexing is added.

Related: [[memory/DECISIONS]], [[memory/concepts/agent-memory]].
