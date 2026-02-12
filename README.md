# Tlacuilo

_Tlacuilo [tɬɑhkwiloh]_

> Nahuatl -> One Who Writes

Simple ToDo Printing for ESC/POS Printers

## Usage

```bash
uv sync
uv run tlacuilo
```

## Templates

Jinja2 templates in `templates/` (user) or `src/tlacuilo/templates/builtin/`.

### `p` object

| Method          | Description                 |
| --------------- | --------------------------- |
| `p.text(str)`   | Print text (max 4000 chars) |
| `p.set(**opts)` | Set formatting              |
| `p.feed(n)`     | Feed n lines (0-50)         |
| `p.cut()`       | Cut paper                   |

### `p.set()` options

| Option          | Values                               |
| --------------- | ------------------------------------ |
| `align`         | `"left"`, `"center"`, `"right"`      |
| `font`          | `"a"`, `"b"`                         |
| `bold`          | bool                                 |
| `underline`     | 0-2                                  |
| `double_height` | bool                                 |
| `double_width`  | bool                                 |
| `custom_size`   | bool (requires `width`/`height` 1-8) |
| `density`       | 0-8                                  |
| `invert`        | bool                                 |
| `smooth`        | bool                                 |
| `flip`          | bool                                 |

### `figlet(text, font="small")`

ASCII art text. Returns string.

```jinja
{{ p.text(figlet("TODO")) }}
{{ p.text(figlet("HI", "banner")) }}
```
