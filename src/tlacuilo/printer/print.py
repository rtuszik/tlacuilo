# tlacuilo/printer/print.py
from __future__ import annotations

from pathlib import Path
from typing import Any

from jinja2 import FileSystemLoader
from jinja2.sandbox import SandboxedEnvironment

from tlacuilo.printer.buffer import PrintBuffer


def _safe_template_name(name: str) -> str:
    if "/" in name or "\\" in name or ".." in name:
        raise ValueError("invalid template name")
    if not name.endswith(".j2"):
        raise ValueError("template must end with .j2")
    return name


def render_template_to_ops(
    *,
    template_name: str,
    context: dict[str, Any],
    user_templates_dir: Path,
    builtin_templates_dir: Path,
) -> list[tuple[str, Any]]:
    template_name = _safe_template_name(template_name)

    env = SandboxedEnvironment(
        loader=FileSystemLoader([str(user_templates_dir), str(builtin_templates_dir)]),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    buf = PrintBuffer()
    env.get_template(template_name).render(p=buf, **context)
    return buf.ops


def execute(printer: Any, ops: list[tuple[str, Any]]) -> None:
    for op, arg in ops:
        if op == "set":
            printer.set(**arg)
        elif op == "text":
            printer.text(arg)
        elif op == "ln":
            printer.ln(arg)
        elif op == "cut":
            printer.cut()
        else:
            raise ValueError(f"unsupported op: {op}")


def render_and_execute_template(
    *,
    printer: Any,
    template_name: str,
    context: dict[str, Any],
    user_templates_dir: Path,
    builtin_templates_dir: Path,
) -> None:
    ops = render_template_to_ops(
        template_name=template_name,
        context=context,
        user_templates_dir=user_templates_dir,
        builtin_templates_dir=builtin_templates_dir,
    )
    execute(printer, ops)
