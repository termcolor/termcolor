from __future__ import annotations

import os
from typing import Any

import pytest

from termcolor import ATTRIBUTES, COLORS, HIGHLIGHTS, colored, cprint, termcolor

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
    monkeypatch.setattr("sys.stdout.isatty", lambda: True)

    # Act / Assert
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
def test_color(
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
    color: str,
    expected: str,
) -> None:
    # Arrange
    monkeypatch.setattr("sys.stdout.isatty", lambda: True)

    # Act / Assert
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
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
    on_color: str,
    expected: str,
) -> None:
    # Arrange
    monkeypatch.setattr("sys.stdout.isatty", lambda: True)

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
    ],
)
def test_attrs(
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
    attr: str,
    expected: str,
) -> None:
    # Arrange
    monkeypatch.setattr("sys.stdout.isatty", lambda: True)

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
    "test_env_vars, expected",
    [
        (["ANSI_COLORS_DISABLED=1"], False),
        (["NO_COLOR=1"], False),
        (["FORCE_COLOR=1"], True),
        (["ANSI_COLORS_DISABLED=1", "NO_COLOR=1", "FORCE_COLOR=1"], False),
        (["NO_COLOR=1", "FORCE_COLOR=1"], False),
    ],
)
def test_environment_variables(
    monkeypatch: pytest.MonkeyPatch, test_env_vars: str, expected: bool
) -> None:
    """Assert combinations do the right thing"""
    for env_var in test_env_vars:
        name, value = env_var.split("=")
        print(name, value)
        monkeypatch.setenv(name, value)

    assert termcolor._can_do_colour() == expected


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
    monkeypatch.setattr("sys.stdout.isatty", lambda: test_isatty)

    # Act / Assert
    assert colored("text", color="cyan") == expected


def test_all_deprecation() -> None:
    """Assert that __ALL__ is deprecated (use __all__ instead)"""
    with pytest.deprecated_call():
        assert termcolor.__ALL__
