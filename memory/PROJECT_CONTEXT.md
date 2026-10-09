---
id: MEM-CONTEXT
type: context
updated: '2026-10-09'
current_phase: 0
phase_status: completed_pending_review
current_phase_authorized: true
next_phase: 1
next_phase_authorized: false
next_action: await_phase_approval
authorization_ref: memory/sessions/2026-10-09-phase-0.md
---
# Project context

## Objective and requirements

Build the Quarterly Technology Intelligence Magazine: continuous AI-assisted
technology research producing an engaging quarterly magazine for business
readers with technical depth for developers, engineers, and researchers.
The user-stated baseline is [[PROJECT_BRIEF]]; this summary does not replace it.

Permanent categories: Artificial Intelligence; Machine Learning; Cybersecurity;
Workflows & Automation; Architectures.

- Collect academic papers, reputable news, official announcements, technical
  community discussions, and accessible newsletters. Collect daily, synthesize
  weekly, analyse trends monthly, publish quarterly. Deduplicate reporting and
  preserve research history. See [[memory/concepts/research-pipeline]].
- Every material factual claim needs a valid DOI or URL and independent checking
  against primary evidence where possible. A valid link does not establish
  accuracy. Disputed/high-impact claims require stronger corroboration. Never
  publish unsupported claims as verified facts; retain metadata and verification
  status. See [[memory/concepts/claim-verification]].
- Coverage uses substantive editorial word count: 15% minimum target and normal
  25% maximum per category, three meaningful subtopics per category per quarter
  as a goal, and a configurable 20% single-organization concentration threshold.
  Exceptions require documentation and human approval.
- Story weights: technical significance 30%, industry/societal impact 25%,
  evidence credibility 20%, novelty 15%, quarterly relevance 10%.
- Significant articles explain what happened, why it matters, how it works,
  limitations, and what comes next. Accessible explanations precede technical
  depth; writing must be original, accurate, non-promotional, and not sensational
  or jargon-heavy. See [[memory/concepts/editorial-engine]].
- Professionally formatted, editable `.docx` is the sole required publishing
  format. No Canva. Human approval is mandatory before final publication.
  See [[memory/concepts/word-generation]].

## State and constraints

Phase 0 — Memory Foundation is complete and awaiting review. Phase 1 is not
authorized. This is memory tooling only; no application functionality exists.
The baseline documents' bootstrap-only scope and pending-phase statements are
historical. Prompt 2 authorizes Phase 0 without changing product requirements;
[[memory/sessions/2026-10-09-phase-0]] preserves that authorization.

Prefer simple, modular, economical engineering, Python and open source where
appropriate. Preserve reproducibility, provenance, logging, and human approval;
treat external research as untrusted input and avoid unnecessary infrastructure.
No application architecture or technology stack has been selected.

Memory uses Git-managed Markdown, YAML metadata, wikilinks, selective retrieval,
consolidation, and session handoffs. No full MARM installation, SQLite, vector
database, embeddings, MCP server, or automated code indexing in Phase 0.
See [[memory/concepts/agent-memory]] and [[memory/DECISIONS]].

## Unresolved questions

Audience regions/languages, issue length, source access, retention, category
overlap, word-count and organization attribution, claim materiality,
corroboration standards, scoring scales, cadence timezone/quarter boundaries,
approval roles, correction policy, budget, runtime, and quality thresholds remain
open. These are later-phase questions, not permission to begin feasibility work.

Earlier `docs/` notes contain superseded planning assumptions; [[PROJECT_BRIEF]]
takes precedence. Reconciliation is deferred, and unrelated existing work is
preserved. See [[memory/PROGRESS]] and [[memory/INDEX]].
