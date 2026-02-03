from __future__ import annotations

from typing import Any, Callable

VALIDATOR = Callable[[Any], Any]


def one_of(*options: Any) -> VALIDATOR:
    allowed = set(options)

    def validator(x: Any) -> Any:
        if x not in allowed:
            raise ValueError(f"Value {x} not in allowed options: {allowed}")
        return x

    return validator


def is_bool(x: Any) -> bool:
    if not isinstance(x, bool):
        raise ValueError(f"Value {x} is not a boolean")
    return x


def int_range(low: int, high: int) -> VALIDATOR:
    def validator(x: Any) -> int:
        if not isinstance(x, int) or not (low <= x <= high):
            raise ValueError(f"Value {x} is not in range [{low}, {high}]")
        return x

    return validator


SET_SCHEMA: dict[str, VALIDATOR] = {
    "align": one_of("left", "center", "right"),
    "font": one_of("a", "b"),
    "bold": is_bool,
    "underline": int_range(0, 2),
    "normal_textsize": is_bool,
    "double_height": is_bool,
    "double_width": is_bool,
    ## custom_size cannot be used with double_height or double_width but requires widht and height
    "custom_size": is_bool,
    "width": int_range(1, 8),
    "height": int_range(1, 8),
    "density": int_range(0, 8),
    "invert": is_bool,
    "smooth": is_bool,
    "flip": is_bool,
}


def validate_set_kwargs(kwargs: dict[str, Any]) -> dict[str, Any]:
    unknown_keys = set(kwargs) - set(SET_SCHEMA)
    if unknown_keys:
        raise ValueError(f"Unknown keys in set kwargs: {sorted(unknown_keys)}")
    out: dict[str, Any] = {}
    for key, value in kwargs.items():
        try:
            out[key] = SET_SCHEMA[key](value)
        except ValueError as e:
            raise ValueError(f"Invalid value for {key}: {e}") from None
    _validate_set_combo(out)
    return out


def _validate_set_combo(kv: dict[str, Any]) -> None:
    dh = kv.get("double_height", False)
    dw = kv.get("double_width", False)
    cs = kv.get("custom_size", False)

    if cs and (dh or dw):
        raise ValueError(
            "custom_size cannot be used with double_height or double_width"
        )

    if cs and ("width" not in kv or "height" not in kv):
        raise ValueError("custom_size requires both width and height")

    if not cs and ("width" in kv or "height" in kv):
        raise ValueError("width/height are only allowed when custom_size=true")
