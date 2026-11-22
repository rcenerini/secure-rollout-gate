import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import check_scope


class TestFindStoryBlock(unittest.TestCase):
    CONTENT = """# BACKLOG

#### S1.8 · Verificação de escopo
- **Saída:** `scripts/check_scope.py`
- **Escopo:**
  - `scripts/check_scope.py`
  - `tests/test_check_scope.py`
- **Interface:** texto

#### S1.9 · Registro de fontes
- **Saída:** `docs/refs/SOURCES.md`
"""

    def test_existing_id(self):
        block = check_scope.find_story_block(self.CONTENT, "S1.8")
        self.assertIsNotNone(block)
        self.assertIn("Verificação de escopo", block)
        self.assertNotIn("S1.9", block)

    def test_non_existing_id(self):
        block = check_scope.find_story_block(self.CONTENT, "S9.9")
        self.assertIsNone(block)


class TestParseEscopo(unittest.TestCase):
    def test_extracts_paths(self):
        block = """- **Escopo:**
  - `scripts/check_scope.py`
  - `tests/test_check_scope.py`
- **Interface:** texto
"""
        paths = check_scope.parse_escopo(block)
        self.assertEqual(paths, ["scripts/check_scope.py", "tests/test_check_scope.py"])

    def test_empty_field(self):
        block = "- **Escopo:**\n- **Interface:** texto\n"
        paths = check_scope.parse_escopo(block)
        self.assertIsNone(paths)

    def test_missing_field(self):
        block = "- **Saída:** `scripts/x.py`\n- **Interface:** texto\n"
        paths = check_scope.parse_escopo(block)
        self.assertIsNone(paths)

    def test_ignores_backticks_outside_field(self):
        block = "- **Saída:** `scripts/x.py`\n- **Escopo:**\n- **Interface:** `outro`\n"
        paths = check_scope.parse_escopo(block)
        self.assertIsNone(paths)


class TestEvaluate(unittest.TestCase):
    def test_fixed_allowlist(self):
        scope = {"scripts/check_scope.py"}
        changed = ["docs/HANDOFF.md"]
        result = check_scope.evaluate(scope, changed, check_scope.FIXED_ALLOWLIST)
        self.assertEqual(result, [])

    def test_decisoes_only_when_in_scope(self):
        scope = {"docs/DECISOES.md"}
        changed = ["docs/DECISOES.md"]
        result = check_scope.evaluate(scope, changed, check_scope.FIXED_ALLOWLIST)
        self.assertEqual(result, [])

    def test_decisoes_outside_when_not_in_scope(self):
        scope = {"scripts/check_scope.py"}
        changed = ["docs/DECISOES.md"]
        result = check_scope.evaluate(scope, changed, check_scope.FIXED_ALLOWLIST)
        self.assertEqual(result, ["docs/DECISOES.md"])

    def test_mixed(self):
        scope = {"scripts/check_scope.py"}
        changed = ["scripts/check_scope.py", "docs/HANDOFF.md", "README.md"]
        result = check_scope.evaluate(scope, changed, check_scope.FIXED_ALLOWLIST)
        self.assertEqual(result, ["README.md"])

    def test_subset(self):
        scope = {"scripts/check_scope.py", "tests/test_check_scope.py"}
        changed = ["scripts/check_scope.py"]
        result = check_scope.evaluate(scope, changed, check_scope.FIXED_ALLOWLIST)
        self.assertEqual(result, [])


class TestIntegration(unittest.TestCase):
    BACKLOG = """#### S1.8 · Verificação de escopo
- **Escopo:**
  - `scripts/check_scope.py`
  - `tests/test_check_scope.py`

#### S1.3 · opencode.json
- **Saída:** `opencode.json`
"""

    @patch("check_scope.run_git_diff")
    @patch("check_scope.read_backlog")
    def test_code_0_within_scope(self, mock_read, mock_diff):
        mock_read.return_value = self.BACKLOG
        mock_diff.return_value = ["scripts/check_scope.py"]
        code = check_scope.main(["--story", "S1.8"])
        self.assertEqual(code, 0)

    @patch("check_scope.run_git_diff")
    @patch("check_scope.read_backlog")
    def test_code_1_outside_scope(self, mock_read, mock_diff):
        mock_read.return_value = self.BACKLOG
        mock_diff.return_value = ["README.md"]
        code = check_scope.main(["--story", "S1.8"])
        self.assertEqual(code, 1)

    @patch("check_scope.run_git_diff")
    @patch("check_scope.read_backlog")
    def test_code_2_no_escopo(self, mock_read, mock_diff):
        mock_read.return_value = self.BACKLOG
        mock_diff.return_value = ["opencode.json"]
        code = check_scope.main(["--story", "S1.3"])
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
