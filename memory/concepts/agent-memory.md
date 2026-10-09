---
id: CON-AGENT-MEMORY
type: concept
updated: '2026-10-09'
---
# Agent Memory

## Purpose and inspiration

Persistent repository notes retain useful context across tasks. The
[MARM README](https://github.com/Lyellr88/marm-memory), reviewed 2026-10-09,
describes persistent memories, concept relationships, and consolidation. We adapt
those ideas into Markdown, with task-specific retrieval and session handoffs as
requested in Prompt 2. This is not a MARM installation or compatibility layer.

## Retrieval and synchronization

Follow [AGENTS.md](../../AGENTS.md): Level 1 core state first, Level 2 relevant
concepts/ADRs second, Level 3 detailed specifications/evidence only as needed.
Search filenames or targeted text rather than loading the vault wholesale.
At meaningful task completion (including partial/blocked tasks), update state,
decisions and concepts, consolidate duplicates, add a session handoff, refresh
the index, validate, and report. This is an agent protocol, not background code.

## Record conventions

- Open the repository root directly as the Obsidian vault. Use UTF-8 Markdown.
- Core filenames are fixed; concepts use lowercase hyphenated names; ADRs use
  `ADR-NNNN-description.md`; sessions use `YYYY-MM-DD-topic.md`.
- Every Markdown file under `memory/` starts with YAML frontmatter containing
  nonempty `id`, `type`, and ISO `updated` date. IDs are unique and immutable:
  `MEM-*`, `CON-*`, `ADR-NNNN`, `SES-*`, or `TEST-*` as appropriate.
- Supported types: index, context, progress, concept, decision, session, archive,
  report. Metadata must be a mapping with unique string keys; unsafe YAML tags
  are rejected by the safe parser.
- Use repository-root-relative wikilinks with exact casing, optional `.md` and
  display alias. Use full paths for unambiguous resolution. Ordinary relative
  Markdown links reference scripts and other files. Metadata `references` is
  an optional list of repository-relative file paths.
- The validator supports file-level wikilinks (including aliases), inline
  Markdown links and images, and Markdown reference links. Heading/block
  fragments are not supported in memory links; use file-level links instead.
  Code fences and inline code examples are excluded from link scanning.
- Add reciprocal links when both concepts explain the relationship. Do not
  generate all-to-all links. Diagram edges alone are not navigable relationships.
- Decisions require status proposed, approved, rejected, or superseded. Approved
  and superseded decisions require an `approval_ref` to a repository record;
  superseded decisions also need `superseded_by` containing the replacement ADR
  ID. Keep rationale, alternatives, consequences, and authority in their bodies.

## State and approval convention

`INDEX`, `PROJECT_CONTEXT`, and `PROGRESS` share identical state fields:
`current_phase` (0–7), `phase_status` (in_progress, blocked,
completed_pending_review, approved), `current_phase_authorized` (true),
`next_phase` (current + 1, or null at Phase 7), `next_phase_authorized` (boolean),
`next_action`, and `authorization_ref` (file recording the user authorization).

An in-progress phase uses `finish_phase_N`; a blocked phase uses
`resolve_blockers`; completed work awaiting review uses `await_phase_approval`.
An approved phase awaiting next-phase authorization uses
`await_next_phase_authorization`. Only an approved phase with explicit next-phase
authorization may use `begin_phase_N`; provide `next_authorization_ref` in all
three core notes. An approved phase needs `phase_approval_ref`. An approved final
phase uses `planning_complete`. Approval references support inspection; the
validator cannot authenticate human approval. Historical sessions do not mirror
live phase fields, so their old state remains historical evidence.

## Consolidation and reproducibility

Promote reusable session knowledge to a canonical concept or ADR and link back
to its provenance. Preserve superseded decisions and archive useful old records;
do not silently overwrite approved policy. Keep summaries concise, omit transient
reasoning, and record unresolved conflicts explicitly. Update backlinks after
renames and never reuse IDs.

Memory files and tooling belong in Git with ordinary reviewed changes. No
automatic commits, hooks, services, indexing, SQLite, vectors, or embeddings.
The initial files are uncommitted until the normal review/commit step.

Python 3.11 and PyYAML 6.0.2 were used locally. For a new environment, use a local
environment and install [requirements-memory.txt](../../requirements-memory.txt)
under its normal dependency approval policy. Run from the repository root:

```text
python -B scripts/validate_memory.py
python -B -m unittest discover -s tests -v
```

The validator also accepts `--root PATH`. It reports structural/link/state errors
and exits nonzero; it does not check external URLs, factual accuracy, approval
authenticity, semantic completeness, Git commit state, or rendered Obsidian UI.

Relationships: [[memory/INDEX]], [[memory/DECISIONS]],
[[memory/decisions/ADR-0001-markdown-memory]],
[[memory/decisions/ADR-0002-memory-conventions]],
[[memory/sessions/2026-10-09-phase-0]], [[memory/archive/README]],
[[memory/PROJECT_CONTEXT]].
