import pytest

from tlacuilo.printer.buffer import PrintBuffer


def test_print_buffer_set():
    buff = PrintBuffer()

    buff.set(align="center").set(bold=True)

    assert len(buff.ops) == 2
    assert buff.ops[0] == ("set", {"align": "center"})
    assert buff.ops[1] == ("set", {"bold": True})


def test_print_buffer_set_invalid():
    buff = PrintBuffer()

    with pytest.raises(ValueError):
        buff.set(align="top")


def test_print_buffer_text():
    buff = PrintBuffer()

    buff.text("Hello, World!")

    assert len(buff.ops) == 1
    assert buff.ops[0] == ("text", "Hello, World!")


def test_print_buffer_text_too_long():
    buff = PrintBuffer()

    with pytest.raises(ValueError, match="text too long"):
        buff.text("A" * 5000)


def test_print_buffer_feed():
    buff = PrintBuffer()

    buff.feed(5)
    assert len(buff.ops) == 1
    assert buff.ops[0] == ("ln", 5)


def test_print_buffer_feed_invalid():
    buff = PrintBuffer()

    with pytest.raises(ValueError, match="feed must be int in"):
        buff.feed(100)


def test_print_buffer_cut():
    buff = PrintBuffer()

    buff.cut()
    assert len(buff.ops) == 1
    assert buff.ops[0] == ("cut", None)
