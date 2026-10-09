# Requirements baseline

Baseline date: 2026-10-09 (Asia/Kuala_Lumpur).
Status: user-stated requirements preserved; application implementation deferred.

## Product vision

Build an AI agent that continuously researches technology developments and produces
a quarterly, magazine-style Microsoft Word document (`.docx`). The magazine must
be accessible and engaging for business readers while maintaining technical depth
for developers, engineers, and researchers.

## Permanent coverage categories

These five categories are permanent:

1. Artificial Intelligence
2. Machine Learning
3. Cybersecurity
4. Workflows & Automation
5. Architectures

## Product requirements

The following requirements describe eventual system behavior, not functionality
already available in this repository.

| ID | Requirement |
| --- | --- |
| REQ-01 | Collect academic papers, reputable news, official announcements, technical community discussions, and accessible newsletters. |
| REQ-02 | Collect sources daily, synthesize weekly, analyse trends monthly, and publish quarterly. |
| REQ-03 | Deduplicate related reporting and preserve historical research. |
| REQ-04 | Independently verify material claims using original evidence and valid DOI/URL references. |
| REQ-05 | Identify trends, rank significant stories, and enforce editorial balance. |
| REQ-06 | Produce original, readable, technically accurate magazine articles. |
| REQ-07 | Generate professionally formatted, editable Microsoft Word documents (`.docx`). |
| REQ-08 | Require human approval before final publication. |
| REQ-09 | Maintain all five permanent coverage categories listed above. |
| REQ-10 | Serve business readers while maintaining technical depth for developers, engineers, and researchers. |

## Research and editorial cadence

| Frequency | Required outcome |
| --- | --- |
| Daily | Collect sources for the research corpus. |
| Weekly | Synthesize collected research. |
| Monthly | Analyse technology trends. |
| Quarterly | Produce the magazine and publish only after human approval. |

Exact execution times, reporting periods, publication deadlines, and scheduling
timezone remain undecided. The date timezone above records this baseline only.
The quarterly cadence does not override the human approval requirement.

## Proposed acceptance evidence

These checks operationalize the requirements for later design and validation;
they are proposals, not completed tests or additional user-approved policy.

| Requirements | Evidence to demonstrate in the implemented system |
| --- | --- |
| REQ-01 | Traceable collected examples from each required source class, with original source references. |
| REQ-02 | Execution records and artifacts demonstrating each cadence. |
| REQ-03 | Related reports grouped without losing their source provenance; earlier research remains retrievable. |
| REQ-04 | Material claims traceable to original evidence and checked DOI/URL references; unresolved claims explicitly surfaced for editorial review. A resolving link alone does not establish support for a claim. |
| REQ-05, REQ-09 | A story selection record showing trend analysis, ranking rationale, and coverage review across the five categories. Balance rules remain to be defined. |
| REQ-06, REQ-10 | Human editorial review of originality, readability, technical accuracy, and suitability for both audience groups. |
| REQ-07 | An editable `.docx` that opens correctly in Microsoft Word and passes a visual layout review against an agreed magazine template. |
| REQ-08 | A final-publication attempt without approval is blocked; an approved issue can proceed through the agreed publication process. |

## Current task boundary

In scope now: initialize project documentation and preserve requirements.

Deferred: application code, prototypes, infrastructure, dependency installation,
source ingestion, research execution, scheduling, model integration, document
generation, and publication. No technology stack, vendor, budget, source list,
ranking formula, or editorial quota is approved by this baseline.

## Requirement changes

Keep requirement IDs stable so later designs and validation can reference them.
Record approved changes here with their date and rationale. Keep proposals and
unresolved decisions separate from confirmed requirements. Existing research
skills are optional tooling; their presence does not establish product scope or
authorize autonomous research runs.

| Date | Change | Basis |
| --- | --- | --- |
| 2026-10-09 | Created initial requirements baseline. | User's product vision and initialization-only instruction. |
