"""Validate the small Markdown memory vault without changing any files."""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required; install requirements-memory.txt in your environment.")


CORE = ("memory/INDEX.md", "memory/PROJECT_CONTEXT.md", "memory/PROGRESS.md")
REQUIRED_FILES = (*CORE, "AGENTS.md", "PROJECT_BRIEF.md", "DEVELOPMENT_PLAN.md",
                  "memory/DECISIONS.md", "memory/archive/README.md",
                  "scripts/validate_memory.py", "tests/test_validate_memory.py",
                  "requirements-memory.txt", "memory/CONTEXT_RECOVERY_REPORT.md",
                  *(f"memory/concepts/{name}.md" for name in (
                      "research-pipeline", "claim-verification", "editorial-engine",
                      "word-generation", "agent-memory")))
REQUIRED_DIRS = ("memory/concepts", "memory/decisions", "memory/sessions", "memory/archive")
TYPES = {"index", "context", "progress", "concept", "decision", "session", "archive", "report"}
STATUSES = {"proposed", "approved", "rejected", "superseded"}
STATE_FIELDS = ("current_phase", "phase_status", "current_phase_authorized", "next_phase",
                "next_phase_authorized", "next_action", "authorization_ref",
                "phase_approval_ref", "next_authorization_ref")


class UniqueSafeLoader(yaml.SafeLoader):
    """Reject duplicate keys rather than accepting the last silent override."""


def unique_mapping(loader, node):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if not isinstance(key, str) or key in result:
            raise ValueError("metadata keys must be unique strings")
        result[key] = loader.construct_object(value_node)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise ValueError("unclosed YAML frontmatter") from None
    data = yaml.load("\n".join(lines[1:end]), Loader=UniqueSafeLoader)
    if not isinstance(data, dict):
        raise ValueError("metadata must be a mapping")
    for field in ("id", "type", "updated"):
        if not isinstance(data.get(field), str) or not data[field].strip():
            raise ValueError(f"{field} must be a nonempty string (quote dates)")
    if not re.fullmatch(r"[A-Z][A-Z0-9-]*", data["id"]):
        raise ValueError("id must use uppercase letters, digits and hyphens")
    date.fromisoformat(data["updated"])
    if not isinstance(data["type"], str) or data["type"] not in TYPES:
        raise ValueError("unknown record type")
    return data, "\n".join(lines[end + 1:])


def prose_only(body):
    # Fences and inline examples do not create navigable graph edges.
    lines = []
    fence = None
    for line in body.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match[1]
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return re.sub(r"(`+).*?\1", "", "\n".join(lines))


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    for name in REQUIRED_FILES:
        if not (root / name).is_file():
            errors.append(f"missing required file: {name}")
    for name in REQUIRED_DIRS:
        if not (root / name).is_dir():
            errors.append(f"missing required directory: {name}")

    def check_file(target, source, relative=False):
        if not isinstance(target, str) or not target.strip():
            errors.append(f"{source}: file reference must be a nonempty string")
            return
        target = unquote(target.strip())
        if "#" in target or "?" in target:
            errors.append(f"{source}: use file-level links without fragments/query: {target}")
            return
        base = (root / source).parent if relative else root
        path = (base / target).resolve()
        if Path(target).is_absolute() or not path.is_relative_to(root):
            errors.append(f"{source}: reference escapes repository: {target}")
        elif not path.is_file():
            errors.append(f"{source}: missing referenced file: {target}")
        else:
            parent = root
            for part in path.relative_to(root).parts:
                if part not in {child.name for child in parent.iterdir()}:
                    errors.append(f"{source}: reference casing does not match file: {target}")
                    break
                parent = parent / part

    records = {}
    ids = {}
    for path in sorted((root / "memory").rglob("*.md")):
        source = path.relative_to(root).as_posix()
        try:
            data, body = frontmatter(path.read_text(encoding="utf-8"))
        except (ValueError, yaml.YAMLError, OSError, UnicodeError) as exc:
            errors.append(f"{source}: invalid metadata: {exc}")
            continue
        records[source] = data
        record_id = data["id"]
        if record_id in ids:
            errors.append(f"{source}: duplicate ID {record_id} (also {ids[record_id]})")
        else:
            ids[record_id] = source

        if source.startswith("memory/decisions/") and data["type"] != "decision":
            errors.append(f"{source}: ADR must have decision type")
        if data["type"] == "decision":
            if not re.fullmatch(r"ADR-\d{4}", record_id) or not path.stem.startswith(record_id + "-"):
                errors.append(f"{source}: ADR ID and filename must agree")
            if not isinstance(data.get("status"), str) or data["status"] not in STATUSES:
                errors.append(f"{source}: invalid decision status")
            if data.get("status") in ("approved", "superseded") and not data.get("approval_ref"):
                errors.append(f"{source}: approved decision requires approval_ref")

        references = data.get("references", [])
        if not isinstance(references, list):
            errors.append(f"{source}: references must be a list")
            references = []
        for target in references:
            check_file(target, source)
        for field in ("authorization_ref", "approval_ref", "phase_approval_ref", "next_authorization_ref"):
            if field in data:
                check_file(data[field], source)

        prose = prose_only(body)
        for link in re.findall(r"\[\[([^\]\n]+)\]\]", prose):
            target = link.split("|", 1)[0].strip()
            if not target.endswith(".md"):
                target += ".md"
            check_file(target, source)
        prose = re.sub(r"\[\[[^\]\n]+\]\]", "", prose)

        # Small, documented Markdown subset: inline and full/collapsed reference links.
        definitions = dict(re.findall(r"(?m)^\s{0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)", prose))
        definitions = {key.casefold(): value for key, value in definitions.items()}
        inline = re.findall(r"\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\)", prose)
        targets = list(definitions.values()) + inline
        for label, ref in re.findall(r"\[([^\]\n]+)\]\[([^\]\n]*)\]", prose):
            key = (ref or label).casefold()
            if key not in definitions:
                errors.append(f"{source}: undefined Markdown reference: {key}")
        for target in targets:
            target = target.strip("<>")
            try:
                if urlsplit(target).scheme in {"https", "http", "mailto"}:
                    continue
            except ValueError:
                errors.append(f"{source}: malformed link: {target}")
                continue
            check_file(target, source, relative=True)

    for source, data in records.items():
        if data.get("type") == "decision" and data.get("status") == "superseded":
            replacement = data.get("superseded_by")
            replacement_path = ids.get(replacement) if isinstance(replacement, str) else None
            if (not replacement_path or replacement == data["id"]
                    or records[replacement_path].get("type") != "decision"
                    or records[replacement_path].get("status") not in ("approved", "superseded")):
                errors.append(f"{source}: superseded_by must reference another approved/superseded ADR")

    for directory, kind in (("decisions", "decision"), ("sessions", "session")):
        if not any(name.startswith(f"memory/{directory}/") and data["type"] == kind
                   for name, data in records.items()):
            errors.append(f"memory/{directory}: at least one {kind} record required")

    if all(name in records for name in CORE):
        state = records[CORE[0]]
        for name in CORE[1:]:
            for field in STATE_FIELDS:
                if records[name].get(field) != state.get(field):
                    errors.append(f"{name}: inconsistent phase/approval field {field}")
        for field in STATE_FIELDS[:7]:
            if field not in state:
                errors.append(f"{CORE[0]}: missing phase field {field}")
        phase = state.get("current_phase")
        status = state.get("phase_status")
        if type(phase) is not int or not 0 <= phase <= 7:
            errors.append("invalid current_phase: expected integer 0..7")
        else:
            expected_next = phase + 1 if phase < 7 else None
            if state.get("next_phase") != expected_next or isinstance(state.get("next_phase"), bool):
                errors.append("next_phase must follow current_phase (null after Phase 7)")
            if state.get("current_phase_authorized") is not True or not state.get("authorization_ref"):
                errors.append("current phase requires authorization and authorization_ref")
            if type(state.get("next_phase_authorized")) is not bool:
                errors.append("next_phase_authorized must be boolean")
            expected_action = {"in_progress": f"finish_phase_{phase}", "blocked": "resolve_blockers",
                               "completed_pending_review": "await_phase_approval",
                               "approved": "await_next_phase_authorization"}.get(status) if isinstance(status, str) else None
            if not expected_action:
                errors.append("invalid phase_status")
            if status == "approved" and not state.get("phase_approval_ref"):
                errors.append("approved phase requires phase_approval_ref")
            if state.get("next_phase_authorized") is True:
                if status != "approved" or phase == 7 or not state.get("next_authorization_ref"):
                    errors.append("next phase requires approved current phase and explicit authorization reference")
                expected_action = f"begin_phase_{expected_next}"
            elif phase == 7 and status == "approved":
                expected_action = "planning_complete"
            if expected_action and state.get("next_action") != expected_action:
                errors.append(f"next_action must be {expected_action}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate(args.root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Memory validation passed: required paths, metadata, IDs, links, ADRs, and phase state.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
