# ReportGenerator

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
