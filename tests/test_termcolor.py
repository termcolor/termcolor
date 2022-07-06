from __future__ import annotations

import os
from typing import Any

import pytest

from termcolor import ATTRIBUTES, COLORS, HIGHLIGHTS, colored, cprint

ALL_COLORS = [*COLORS, None]
ALL_HIGHLIGHTS = [*HIGHLIGHTS, None]
ALL_ATTRIBUTES = [*ATTRIBUTES, None]


def setup_module() -> None:
    # By default, make sure no env vars already set for tests
    try:
        del os.environ["ANSI_COLORS_DISABLED"]
    except KeyError:  # pragma: no cover
        pass


def test_basic() -> None:
    assert colored("text") == "text\x1b[0m"


def test_sanity() -> None:
    for color in ALL_COLORS:
        for highlight in ALL_HIGHLIGHTS:
            for attribute in ALL_ATTRIBUTES:
                attrs = None if attribute is None else [attribute]
                colored("text", color, highlight, attrs)
                cprint("text", color, highlight, attrs)


def assert_cprint(
    capsys: pytest.CaptureFixture[str],
    expected: str,
    text: str,
    color: str | None = None,
    on_color: str | None = None,
    attrs: list[str] | None = None,
    **kwargs: Any,
) -> None:
    cprint(text, color, on_color, attrs, **kwargs)
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == expected + "\n"


@pytest.mark.parametrize(
    "color, expected",
    [
        ("grey", "\x1b[30mtext\x1b[0m"),
        ("red", "\x1b[31mtext\x1b[0m"),
        ("green", "\x1b[32mtext\x1b[0m"),
        ("yellow", "\x1b[33mtext\x1b[0m"),
        ("blue", "\x1b[34mtext\x1b[0m"),
        ("magenta", "\x1b[35mtext\x1b[0m"),
        ("cyan", "\x1b[36mtext\x1b[0m"),
        ("white", "\x1b[37mtext\x1b[0m"),
    ],
)
def test_color(capsys: pytest.CaptureFixture[str], color: str, expected: str) -> None:
    assert colored("text", color=color) == expected
    assert_cprint(capsys, expected, "text", color=color)


@pytest.mark.parametrize(
    "on_color, expected",
    [
        ("on_grey", "\x1b[40mtext\x1b[0m"),
        ("on_red", "\x1b[41mtext\x1b[0m"),
        ("on_green", "\x1b[42mtext\x1b[0m"),
        ("on_yellow", "\x1b[43mtext\x1b[0m"),
        ("on_blue", "\x1b[44mtext\x1b[0m"),
        ("on_magenta", "\x1b[45mtext\x1b[0m"),
        ("on_cyan", "\x1b[46mtext\x1b[0m"),
        ("on_white", "\x1b[47mtext\x1b[0m"),
    ],
)
def test_on_color(
    capsys: pytest.CaptureFixture[str], on_color: str, expected: str
) -> None:
    assert colored("text", on_color=on_color) == expected
    assert_cprint(capsys, expected, "text", on_color=on_color)


@pytest.mark.parametrize(
    "attr, expected",
    [
        ("bold", "\x1b[1mtext\x1b[0m"),
        ("dark", "\x1b[2mtext\x1b[0m"),
        ("underline", "\x1b[4mtext\x1b[0m"),
        ("blink", "\x1b[5mtext\x1b[0m"),
        ("reverse", "\x1b[7mtext\x1b[0m"),
        ("concealed", "\x1b[8mtext\x1b[0m"),
    ],
)
def test_attrs(capsys: pytest.CaptureFixture[str], attr: str, expected: str) -> None:
    assert colored("text", attrs=[attr]) == expected
    assert_cprint(capsys, expected, "text", attrs=[attr])


@pytest.mark.parametrize(
    "test_env_var",
    [
        "ANSI_COLORS_DISABLED",
        "NO_COLOR",
    ],
)
@pytest.mark.parametrize(
    "test_value",
    [
        "true",
        "false",
        "1",
        "0",
        "",
    ],
)
def test_env_var(
    monkeypatch: pytest.MonkeyPatch, test_env_var: str, test_value: str
) -> None:
    """Assert nothing applied when this env var set, regardless of value."""
    monkeypatch.setenv(test_env_var, test_value)
    assert colored("text", color="red") == "text"
