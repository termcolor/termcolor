from __future__ import annotations

import os
from collections.abc import Iterable
from typing import Any

import pytest

from termcolor import ATTRIBUTES, COLORS, HIGHLIGHTS, colored, cprint, termcolor
from termcolor._types import Attribute, Color, Highlight

ALL_COLORS = [*COLORS, None]
ALL_HIGHLIGHTS = [*HIGHLIGHTS, None]
ALL_ATTRIBUTES = [*ATTRIBUTES, None]


def setup_module() -> None:
    # By default, make sure no env vars already set for tests
    for var in ("ANSI_COLORS_DISABLED", "NO_COLOR", "FORCE_COLOR"):
        try:
            del os.environ[var]
        except KeyError:  # pragma: no cover
            pass


def test_basic(monkeypatch: pytest.MonkeyPatch) -> None:
    # Arrange
    monkeypatch.setattr(os, "isatty", lambda fd: True)
    monkeypatch.setattr("sys.stdout.isatty", lambda: True)
    monkeypatch.setattr("sys.stdout.fileno", lambda: 1)

    # Act / Assert
    assert colored("text") == "text\x1b[0m"


def test_sanity() -> None:
    for color in ALL_COLORS:
        for highlight in ALL_HIGHLIGHTS:
            for attribute in ALL_ATTRIBUTES:
                attrs = None if attribute is None else [attribute]
                colored("text", color, highlight, attrs)
                cprint("text", color, highlight, attrs)
                colored("text", color, highlight, attrs, no_color=True)
                cprint("text", color, highlight, attrs, no_color=True)
                colored("text", color, highlight, attrs, force_color=True)
                cprint("text", color, highlight, attrs, force_color=True)


def assert_cprint(
    capsys: pytest.CaptureFixture[str],
    expected: str,
    text: str,
    color: Color | None = None,
    on_color: Highlight | None = None,
    attrs: Iterable[Attribute] | None = None,
    **kwargs: Any,
) -> None:
    cprint(text, color, on_color, attrs, **kwargs)
    captured = capsys.readouterr()
    print(captured.out)
    assert captured.out == expected + "\n"


@pytest.mark.parametrize(
    "color, expected",
    [
        ("black", "\x1b[30mtext\x1b[0m"),
        ("grey", "\x1b[30mtext\x1b[0m"),
        ("red", "\x1b[31mtext\x1b[0m"),
        ("green", "\x1b[32mtext\x1b[0m"),
        ("yellow", "\x1b[33mtext\x1b[0m"),
        ("blue", "\x1b[34mtext\x1b[0m"),
        ("magenta", "\x1b[35mtext\x1b[0m"),
        ("cyan", "\x1b[36mtext\x1b[0m"),
        ("white", "\x1b[97mtext\x1b[0m"),
        ("light_grey", "\x1b[37mtext\x1b[0m"),
        ("dark_grey", "\x1b[90mtext\x1b[0m"),
        ("light_blue", "\x1b[94mtext\x1b[0m"),
    ],
)
def test_color(
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
    color: Color,
    expected: str,
) -> None:
    # Arrange
    monkeypatch.setattr(os, "isatty", lambda fd: True)
    monkeypatch.setattr("sys.stdout.isatty", lambda: True)
    monkeypatch.setattr("sys.stdout.fileno", lambda: 1)

    # Act / Assert
    assert colored("text", color=color) == expected
    assert_cprint(capsys, expected, "text", color=color)


@pytest.mark.parametrize(
    "on_color, expected",
    [
        ("on_black", "\x1b[40mtext\x1b[0m"),
        ("on_grey", "\x1b[40mtext\x1b[0m"),
        ("on_red", "\x1b[41mtext\x1b[0m"),
        ("on_green", "\x1b[42mtext\x1b[0m"),
        ("on_yellow", "\x1b[43mtext\x1b[0m"),
        ("on_blue", "\x1b[44mtext\x1b[0m"),
        ("on_magenta", "\x1b[45mtext\x1b[0m"),
        ("on_cyan", "\x1b[46mtext\x1b[0m"),
        ("on_white", "\x1b[107mtext\x1b[0m"),
        ("on_light_grey", "\x1b[47mtext\x1b[0m"),
        ("on_dark_grey", "\x1b[100mtext\x1b[0m"),
        ("on_light_blue", "\x1b[104mtext\x1b[0m"),
    ],
)
def test_on_color(
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
    on_color: Highlight,
    expected: str,
) -> None:
    # Arrange
    monkeypatch.setattr(os, "isatty", lambda fd: True)
    monkeypatch.setattr("sys.stdout.isatty", lambda: True)
    monkeypatch.setattr("sys.stdout.fileno", lambda: 1)

    # Act / Assert
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
        ("strike", "\x1b[9mtext\x1b[0m"),
    ],
)
def test_attrs(
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
    attr: Attribute,
    expected: str,
) -> None:
    # Arrange
    monkeypatch.setattr(os, "isatty", lambda fd: True)
    monkeypatch.setattr("sys.stdout.isatty", lambda: True)
    monkeypatch.setattr("sys.stdout.fileno", lambda: 1)

    # Act / Assert
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
def test_environment_variables_disable_color(
    monkeypatch: pytest.MonkeyPatch, test_env_var: str, test_value: str
) -> None:
    """Assert nothing applied when this env var set, regardless of value"""
    monkeypatch.setenv(test_env_var, test_value)
    assert colored("text", color="cyan") == "text"


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
def test_environment_variables_force_color(
    monkeypatch: pytest.MonkeyPatch, test_value: str
) -> None:
    """Assert color applied when this env var set, regardless of value"""
    monkeypatch.setenv("FORCE_COLOR", test_value)
    assert colored("text", color="cyan") == "\x1b[36mtext\x1b[0m"


@pytest.mark.parametrize(
    "test_no_color, test_force_color, test_env_vars, expected",
    [
        # Set only env vars
        (None, None, ["ANSI_COLORS_DISABLED=1"], False),
        (None, None, ["NO_COLOR=1"], False),
        (None, None, ["FORCE_COLOR=1"], True),
        (None, None, ["ANSI_COLORS_DISABLED=1", "NO_COLOR=1", "FORCE_COLOR=1"], False),
        (None, None, ["NO_COLOR=1", "FORCE_COLOR=1"], False),
        (None, None, ["TERM=dumb"], False),
        # Set only parameter overrides
        (True, None, [None], False),
        (None, True, [None], True),
        (True, True, [None], False),
        # Set both parameter overrides and env vars
        (True, None, ["NO_COLOR=1"], False),
        (None, True, ["NO_COLOR=1"], True),
        (True, True, ["NO_COLOR=1"], False),
        (True, None, ["FORCE_COLOR=1"], False),
        (None, True, ["FORCE_COLOR=1"], True),
        (True, True, ["FORCE_COLOR=1"], False),
    ],
)
def test_environment_variables(
    monkeypatch: pytest.MonkeyPatch,
    test_no_color: bool,
    test_force_color: bool,
    test_env_vars: str,
    expected: bool,
) -> None:
    """Assert combinations do the right thing"""
    for env_var in test_env_vars:
        if not env_var:
            continue
        name, value = env_var.split("=")
        print(f"{name}={value}")
        monkeypatch.setenv(name, value)

    assert (
        termcolor._can_do_colour(no_color=test_no_color, force_color=test_force_color)
        == expected
    )


@pytest.mark.parametrize(
    "test_isatty, expected",
    [
        (True, "\x1b[36mtext\x1b[0m"),
        (False, "text"),
    ],
)
def test_tty(monkeypatch: pytest.MonkeyPatch, test_isatty: bool, expected: str) -> None:
    """Assert color when attached to tty, no color when not attached"""
    # Arrange
    monkeypatch.setattr(os, "isatty", lambda fd: test_isatty)
    monkeypatch.setattr("sys.stdout.isatty", lambda: test_isatty)
    monkeypatch.setattr("sys.stdout.fileno", lambda: 1)

    # Act / Assert
    assert colored("text", color="cyan") == expected


def test_all_deprecation() -> None:
    """Assert that __ALL__ is deprecated (use __all__ instead)"""
    with pytest.deprecated_call():
        assert termcolor.__ALL__
