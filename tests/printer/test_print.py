from pathlib import Path

import pytest
from pyfiglet import FontNotFound

from tlacuilo.printer.print import _figlet, render_template_to_ops


class TestFiglet:
    def test_figlet_default_font(self):
        result = _figlet("HI")
        assert isinstance(result, str)
        assert len(result) > 4
        assert "\n" in result

    def test_figlet_custom_font(self):
        result = _figlet("A", font="banner")
        assert isinstance(result, str)
        assert "\n" in result

    def test_figlet_invalid_font(self):
        with pytest.raises(FontNotFound):
            _figlet("test", font="not_a_real_font_12345")


class TestFigletInTemplate:
    def test_figlet_available_in_template(self, tmp_path: Path):
        template_dir = tmp_path / "templates"
        template_dir.mkdir()
        template_file = template_dir / "test_figlet.j2"
        template_file.write_text('{{ p.text(figlet("X")) }}')

        ops = render_template_to_ops(
            template_name="test_figlet.j2",
            context={},
            user_templates_dir=template_dir,
            builtin_templates_dir=template_dir,
        )

        assert len(ops) == 1
        assert ops[0][0] == "text"
        assert isinstance(ops[0][1], str)
        assert len(ops[0][1]) > 1

    def test_figlet_with_custom_font_in_template(self, tmp_path: Path):
        template_dir = tmp_path / "templates"
        template_dir.mkdir()
        template_file = template_dir / "test_figlet_font.j2"
        template_file.write_text('{{ p.text(figlet("Y", "small")) }}')

        ops = render_template_to_ops(
            template_name="test_figlet_font.j2",
            context={},
            user_templates_dir=template_dir,
            builtin_templates_dir=template_dir,
        )

        assert len(ops) == 1
        assert ops[0][0] == "text"
