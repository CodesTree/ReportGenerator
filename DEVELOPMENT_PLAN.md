# Quarterly Technology Intelligence Magazine — Development Plan

Date: 2026-10-09 (Asia/Kuala_Lumpur)  
Status: high-level phase index only; future phases await authorization.

## Planning baseline

[PROJECT_BRIEF.md](PROJECT_BRIEF.md) preserves the current product vision,
requirements, constraints, and open questions. This plan indexes future work; it
is not a complete specification, detailed architecture, or implementation plan.

The current bootstrap consists only of these two documents. It precedes Phase 0
and does not implement the persistent memory system.

## Phase index

| Phase | Focus | Intended deliverable and review scope |
| --- | --- | --- |
| 0 — Memory Foundation | Establish the lightweight, MARM-inspired Markdown project memory in Prompt 2. | Reviewable memory foundation for requirements, decisions, assumptions, unresolved questions, and project progress; exact structure to be defined in Prompt 2. |
| 1 — Feasibility | Research practical feasibility, evidence access, operational constraints, and costs before architecture decisions. | Feasibility findings with sources, risks, uncertainties, and options; no premature stack commitment. |
| 2 — Requirements | Refine the brief into testable product, editorial, evidence, and operating requirements. | Requirements and acceptance criteria, including scoring rubrics, word-count balance rules, verification expectations, and approval procedures. |
| 3 — Architecture | Use approved requirements and feasibility evidence to assess a simple, modular, economical design. | Proposed architecture and decision rationale covering trust boundaries, reproducibility, provenance, logging, and human approval. |
| 4 — Pipelines | Define collection, deduplication, historical preservation, verification, synthesis, trend analysis, story selection, and editorial workflows. | Pipeline responsibilities, cadence, quality gates, and failure/review handling at an agreed planning depth. |
| 5 — Document Generation | Define the quarterly magazine's editable Word output and editorial presentation. | `.docx` layout and generation requirements, article structure, references, and document validation approach; no Canva integration. |
| 6 — Data Models | Consolidate information requirements identified in the preceding phases. | Proposed data models for sources, claims, verification, research history, stories, issues, provenance, and approvals; no storage technology assumed. |
| 7 — Roadmap | Sequence implementation after planning deliverables are reviewed. | Prioritized implementation milestones, dependencies, validation gates, and unresolved risks for approval. |

All phases are pending. Their deliverables are planning intentions, not permission
to begin research, implementation, infrastructure setup, or publication. Any
prototype or implementation work requires explicit authorization in its phase
scope. Earlier phases may identify data needs; Phase 6 consolidates them. Changes
to approved decisions must return through review rather than silently overriding
earlier deliverables.

## Gate for every phase

1. Confirm that the phase and its scope are authorized.
2. Complete only that phase, researching before architectural decisions.
3. Record assumptions, unresolved questions, and supporting evidence in the
   persistent memory once Phase 0 establishes it.
4. Validate deliverables against the brief and the authorized scope.
5. Summarize results, limitations, and decisions needed.
6. Stop and request explicit approval before beginning the next phase.

Human approval before final publication remains mandatory regardless of planning
or implementation approvals.

## Immediate next gate

Review and approve the two bootstrap documents. Then authorize Phase 0 — Memory
Foundation through Prompt 2. No external tool research, detailed system
architecture, production code, or memory-system implementation belongs to the
current bootstrap task.
