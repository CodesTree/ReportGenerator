"""Mutation tests against isolated copies; the real memory vault is never edited."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from scripts.validate_memory import CORE, REQUIRED_FILES, validate

REPO = Path(__file__).resolve().parents[1]


class MemoryValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copytree(REPO / "memory", self.root / "memory")
        for name in REQUIRED_FILES:
            if not name.startswith("memory/"):
                target = self.root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(REPO / name, target)

    def change(self, name, old, new):
        path = self.root / name
        content = path.read_text(encoding="utf-8")
        self.assertIn(old, content)
        path.write_text(content.replace(old, new), encoding="utf-8")

    def append(self, name, text):
        path = self.root / name
        path.write_text(path.read_text(encoding="utf-8") + text, encoding="utf-8")

    def assert_error(self, fragment):
        errors = validate(self.root)
        self.assertTrue(any(fragment in error for error in errors), errors)

    def test_valid_vault(self):
        self.assertEqual([], validate(self.root))

    def test_malformed_yaml(self):
        self.change("memory/INDEX.md", "id: MEM-INDEX", "id: [unterminated")
        self.assert_error("invalid metadata")

    def test_duplicate_yaml_keys(self):
        self.change("memory/INDEX.md", "id: MEM-INDEX", "id: MEM-INDEX\nid: SECOND")
        self.assert_error("unique strings")

    def test_unsafe_yaml_tag(self):
        self.change("memory/INDEX.md", "id: MEM-INDEX", "id: !!python/object:builtins.object {}")
        self.assert_error("invalid metadata")

    def test_missing_metadata(self):
        self.change("memory/INDEX.md", "id: MEM-INDEX\n", "")
        self.assert_error("id must be")

    def test_invalid_date(self):
        self.change("memory/INDEX.md", "'2026-10-09'", "'2026-99-09'")
        self.assert_error("invalid metadata")

    def test_non_scalar_type(self):
        self.change("memory/INDEX.md", "type: index", "type: [index]")
        self.assert_error("invalid metadata")

    def test_phase_approval_requires_evidence(self):
        for name in CORE:
            path = self.root / name
            text = path.read_text(encoding="utf-8")
            import re
            text = re.sub(r"(?m)^phase_status: .*", "phase_status: approved", text)
            text = re.sub(r"(?m)^next_action: .*", "next_action: await_next_phase_authorization", text)
            path.write_text(text, encoding="utf-8")
        self.assert_error("approved phase requires phase_approval_ref")

    def test_explicit_authorization_transition(self):
        for name in CORE:
            path = self.root / name
            text = path.read_text(encoding="utf-8")
            import re
            text = re.sub(r"(?m)^phase_status: .*", "phase_status: approved", text)
            text = re.sub(r"(?m)^next_action: .*", "next_action: begin_phase_1", text)
            text = text.replace("next_phase_authorized: false", "next_phase_authorized: true")
            text = text.replace("id: ", "phase_approval_ref: memory/sessions/2026-10-09-phase-0.md\n"
                                "next_authorization_ref: memory/sessions/2026-10-09-phase-0.md\nid: ", 1)
            path.write_text(text, encoding="utf-8")
        # Structural check only: the validator cannot authenticate approval prose.
        self.assertEqual([], validate(self.root))

    def test_duplicate_record_id(self):
        self.change("memory/PROJECT_CONTEXT.md", "id: MEM-CONTEXT", "id: MEM-INDEX")
        self.assert_error("duplicate ID")

    def test_broken_wikilink(self):
        self.append("memory/INDEX.md", "\n[[memory/missing|Missing]]\n")
        self.assert_error("missing referenced file: memory/missing.md")

    def test_missing_required_file(self):
        (self.root / "memory/PROGRESS.md").unlink()
        self.assert_error("missing required file: memory/PROGRESS.md")

    def test_missing_required_directory(self):
        shutil.rmtree(self.root / "memory/archive")
        self.assert_error("missing required directory: memory/archive")

    def test_missing_markdown_target(self):
        self.append("memory/INDEX.md", "\n[script](../scripts/missing.py)\n")
        self.assert_error("missing referenced file: ../scripts/missing.py")

    def test_missing_metadata_reference(self):
        self.change("memory/INDEX.md", "id: MEM-INDEX", "id: MEM-INDEX\nreferences: [missing.txt]")
        self.assert_error("missing referenced file: missing.txt")

    def test_valid_reference_link(self):
        self.append("memory/INDEX.md", "\n[Brief][baseline]\n[baseline]: ../PROJECT_BRIEF.md\n")
        self.assertEqual([], validate(self.root))

    def test_undefined_reference_link(self):
        self.append("memory/INDEX.md", "\n[Brief][missing]\n")
        self.assert_error("undefined Markdown reference")

    def test_code_examples_ignored(self):
        self.append("memory/INDEX.md", "\n`[[not-a-note]]`\n```text\n[[also-not-a-note]]\n```\n")
        self.assertEqual([], validate(self.root))

    def test_escape_rejected(self):
        self.append("memory/INDEX.md", "\n[escape](../../outside.md)\n")
        self.assert_error("escapes repository")

    def test_invalid_decision_status(self):
        self.change("memory/decisions/ADR-0001-markdown-memory.md", "status: approved", "status: imaginary")
        self.assert_error("invalid decision status")

    def test_approved_decision_requires_evidence(self):
        self.change("memory/decisions/ADR-0001-markdown-memory.md",
                    "approval_ref: memory/sessions/2026-10-09-phase-0.md\n", "")
        self.assert_error("approved decision requires approval_ref")

    def test_superseded_decision_requires_replacement(self):
        self.change("memory/decisions/ADR-0001-markdown-memory.md", "status: approved", "status: superseded")
        self.assert_error("superseded_by")

    def test_inconsistent_phase(self):
        self.change("memory/PROGRESS.md", "current_phase: 0", "current_phase: 1")
        self.assert_error("inconsistent phase/approval field current_phase")

    def test_boolean_phase_is_invalid(self):
        for name in CORE:
            self.change(name, "current_phase: 0", "current_phase: false")
        self.assert_error("invalid current_phase")

    def test_unauthorized_advance(self):
        for name in CORE:
            self.change(name, "next_phase_authorized: false", "next_phase_authorized: true")
        self.assert_error("next phase requires approved current phase")

    def test_cli_failure_exit_code(self):
        (self.root / "AGENTS.md").unlink()
        result = subprocess.run([sys.executable, "-B", str(REPO / "scripts/validate_memory.py"),
                                 "--root", str(self.root)], capture_output=True, text=True)
        self.assertEqual(1, result.returncode)
        self.assertIn("missing required file: AGENTS.md", result.stderr)


if __name__ == "__main__":
    unittest.main()
