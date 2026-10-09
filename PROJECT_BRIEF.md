# Quarterly Technology Intelligence Magazine — Project Brief

Date: 2026-10-09 (Asia/Kuala_Lumpur)  
Status: bootstrap requirements baseline; application implementation not authorized.

## Purpose and authority

Preserve the user-stated product vision and consolidated requirements for an
AI-powered research and editorial system. This is a bootstrap brief, not a
complete specification or an approved technical design.

For this bootstrap, the requirements below take precedence wherever earlier
planning notes in `README.md` or `docs/` differ or leave these requirements
undecided. Those files are unchanged; reconciliation is deferred to an authorized
phase. The phase index is in [DEVELOPMENT_PLAN.md](DEVELOPMENT_PLAN.md).

## Product vision and audience

Build an AI agent that continuously researches technology developments and
produces a quarterly, magazine-style Microsoft Word document (`.docx`). The
magazine must be accessible and engaging for business readers while maintaining
technical depth for developers, engineers, and researchers.

The five permanent coverage categories are:

1. Artificial Intelligence
2. Machine Learning
3. Cybersecurity
4. Workflows & Automation
5. Architectures

## Eventual capabilities and cadence

- Collect academic papers, reputable news, official announcements, technical
  community discussions, and accessible newsletters.
- Collect sources daily, synthesize weekly, analyse trends monthly, and publish
  quarterly, subject to human approval.
- Deduplicate related reporting and preserve historical research.
- Independently verify material claims using original evidence and valid DOI/URL
  references.
- Identify trends, rank significant stories, and enforce editorial balance.
- Produce original, readable, technically accurate magazine articles.
- Generate professionally formatted, editable Word documents.
- Require human approval before final publication.

These describe intended capabilities, not functionality currently implemented.

## Non-negotiable requirements

### Evidence quality

- Every material factual claim must be traceable to a valid DOI or URL.
- Link validity alone is not proof of claim accuracy.
- Independently check claims against primary evidence where possible.
- Require stronger corroboration for disputed or high-impact claims.
- Never publish unsupported claims as verified facts.
- Preserve source metadata and verification status.

### Editorial balance

- Maintain a 15% minimum coverage target per category.
- Apply a normal 25% maximum per category.
- Aim for three meaningful subtopics per category per quarter.
- Use a configurable 20% concentration threshold for any single organization.
- Allow documented, human-approved exceptions to editorial balance rules.
- Calculate coverage from substantive editorial word count.

Precise counting, attribution, and exception procedures remain to be specified;
the stated targets and thresholds are preserved requirements.

### Story scoring

| Criterion | Weight |
| --- | ---: |
| Technical significance | 30% |
| Industry/societal impact | 25% |
| Evidence credibility | 20% |
| Novelty | 15% |
| Quarterly relevance | 10% |
| **Total** | **100%** |

Scoring scales, rubrics, and tie-breaking rules remain open.

### Writing quality

Every significant article must explain:

1. What happened?
2. Why does it matter?
3. How does it work?
4. What are its limitations?
5. What comes next?

Use accessible explanations followed by technical depth. Avoid jargon-heavy,
sensational, or promotional writing.

### Engineering

- Prefer simple, modular, economical architecture.
- Prioritize Python and open-source solutions when appropriate.
- Preserve reproducibility, provenance, logging, and human approval.
- Treat external research as untrusted input.
- Avoid unnecessary infrastructure.
- Produce `.docx` as the sole required publishing format.
- No Canva integration.

No particular framework, provider, database, deployment model, or infrastructure
is selected by this brief.

### Development governance

1. Complete one authorized phase at a time.
2. Research before making architectural decisions.
3. Record assumptions and unresolved questions.
4. Validate deliverables before reporting completion.
5. Stop and request approval before beginning the next phase.
6. Maintain persistent project memory using a lightweight, MARM-inspired Markdown
   system. Implement that memory system in Prompt 2, during Phase 0.

Phase approval and final-publication approval are separate requirements.

## Current authorization and exclusions

The current task creates only `PROJECT_BRIEF.md` and `DEVELOPMENT_PLAN.md`,
validates them, summarizes their contents, and stops for approval.

Do not implement the application or the memory system in this bootstrap. Do not
research external tools, generate detailed architecture, or write production
code. The phase index does not authorize subsequent work.

## Assumptions and unresolved questions

Planning assumptions: the supplied requirements form the current baseline;
Python/open-source preferences do not constitute a finalized stack. No additional
product policy is assumed approved.

Questions to resolve in later authorized phases include:

- What regions, industries, languages, issue length, and article mix are desired?
- How are category overlap, substantive editorial words, meaningful subtopics,
  and organizational attribution counted?
- What defines a material claim or significant article, and what verification
  and corroboration criteria apply?
- What sources are accessible, and what collection and retention limits apply?
- Which timezone, quarter boundaries, and publication deadlines govern cadence?
- Who approves issues and exceptions, and how are revisions and corrections handled?
- What budget, operating environment, research volume, and quality criteria apply?

Resolve these questions through the phase gates; they do not block preservation
of the requirements above.
