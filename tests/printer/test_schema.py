import pytest

from tlacuilo.printer import schema


def test_one_of():
    validator = schema.one_of("left", "center", "right")
    assert validator("left") == "left"

    with pytest.raises(ValueError, match="not in allowed options"):
        validator("top")


def test_is_bool():
    validator = schema.is_bool
    assert validator(True) is True

    with pytest.raises(ValueError, match="is not a boolean"):
        validator(1)


def test_int_range():
    validator = schema.int_range(1, 5)
    assert validator(3) == 3

    with pytest.raises(ValueError, match="is not in range"):
        validator(0)


@pytest.mark.parametrize(
    "kwargs",
    [
        {"align": "left"},
        {"bold": True, "font": "a"},
        {"underline": 1, "invert": False},
        {"custom_size": True, "width": 2, "height": 2},
    ],
)
def test_validate_set_kwargs(kwargs):
    assert schema.validate_set_kwargs(kwargs) == kwargs


@pytest.mark.parametrize(
    "kwargs",
    [
        {"align": "up"},
        {"cursive": "Yes", "width": 3},
    ],
)
def test_validate_set_kwargs_unknown(kwargs):
    with pytest.raises(ValueError):
        schema.validate_set_kwargs(kwargs)


@pytest.mark.parametrize(
    "kwargs",
    [
        {"double_height": True, "custom_size": True, "width": 2, "height": 2},
        {"double_width": True, "custom_size": True, "double_height": False},
        {"custom_size": True, "width": 2},
    ],
)
def test_validate_set_kwargs_invalid_combo(kwargs):
    with pytest.raises(ValueError):
        schema._validate_set_combo(kwargs)
