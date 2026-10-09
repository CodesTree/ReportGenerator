# Quarterly Technology Intelligence Magazine

An AI-powered research and editorial system that will continuously research
technology developments and produce a quarterly, magazine-style, editable
Microsoft Word document (`.docx`). The repository retains the name `ReportGenerator`.

The magazine will be accessible and engaging for business readers while preserving
technical depth for developers, engineers, and researchers.

**Current phase: project initialization and requirements preservation only.**
The application has not been implemented. Research collection, scheduling,
document generation, and publication are not active.

## Project documentation

- [Requirements baseline](docs/requirements.md): product scope, permanent coverage,
  cadence, requirements, and future acceptance criteria.
- [System outline and open decisions](docs/system-outline.md): conceptual
  responsibilities and questions to resolve before implementation.

The requirements baseline is the source of truth for product requirements.
The system outline is planning material, not an approved technical design.
Implementation requires a subsequent explicit request.

## Permanent coverage

1. Artificial Intelligence
2. Machine Learning
3. Cybersecurity
4. Workflows & Automation
5. Architectures

## Editorial cycle

Collect daily, synthesize weekly, analyse trends monthly, and publish quarterly.
Final publication requires human approval.

## AI Research Skills

Orchestra Research's skills are installed for this repository in `.agents/skills/`.
The source revision and complete skill list are recorded in `ai-research-skills.lock.json`.
No global skill installation is required.

To start, send Codex a research question, for example:

> Use autoresearch to investigate [research question] in this repository.

The entry point is `.agents/skills/0-autoresearch-skill/SKILL.md` (skill name: `autoresearch`).
You can also request an individual skill for a specific task, such as a literature-informed
research brainstorm, model evaluation, or paper writing. Installed skills should be
available on the next turn; reopen the session if they are not discovered.

Autoresearch describes continuous research using a 20-minute loop. Its documented
Claude Code and OpenClaw commands are platform-specific; in Codex, recurring work
uses a chat automation when starting a scoped research project. Installation alone
does not start research or schedule recurring work.

The installation includes skill instructions and supporting resources, not every
framework or model mentioned by the skills. Install task-specific dependencies only
when needed, using a repository-local environment.

Upstream setup: https://www.orchestra-research.com/ai-research-skills/welcome.md
