from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from tlacuilo.printer.schema import validate_set_kwargs

MAX_OPS = 100


@dataclass
class PrintBuffer:
    ops: list[tuple[str, Any]] = field(default_factory=list)

    def _append(self, op: str, arg: Any) -> None:
        if len(self.ops) >= MAX_OPS:
            raise ValueError("too many print operations")
        self.ops.append((op, arg))

    def set(self, **kwargs: Any) -> PrintBuffer:
        self._append("set", validate_set_kwargs(kwargs))
        return self

    def text(self, value: Any) -> PrintBuffer:
        s = "" if value is None else str(value)
        if len(s) > 4000:
            raise ValueError("text too long")
        self._append("text", s)
        return self

    def feed(self, n: int = 1) -> PrintBuffer:
        if not isinstance(n, int) or not (0 <= n <= 50):
            raise ValueError("feed must be int in [0..50]")
        self._append("ln", n)
        return self

    def cut(self) -> PrintBuffer:
        self._append("cut", None)
        return self
