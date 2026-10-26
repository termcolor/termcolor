"""Extended coverage for ``termcolor.colored`` / ``cprint`` / ``can_colorize``.

Every assertion below was probed against the shipped implementation
before being written down. Notable current behaviour pinned here:

* When colour is enabled but no code is requested (no colour, highlight
  or attribute), the text is still returned with a trailing RESET
  (``\\x1b[0m``) and no opening escape sequence.
* ``can_colorize`` is wrapped in ``functools.cache``, so a call with no
  arguments remembers its first answer until ``cache_clear()`` -- the
  env-var tests below clear the cache explicitly, otherwise later
  tests would see a stale answer.
* ``grey``/``on_grey`` are aliases of black (30/40), kept for backwards
  compatibility; they are *not* a separate grey.
"""

from __future__ import annotations

import pytest

from termcolor import ATTRIBUTES, COLORS, HIGHLIGHTS, can_colorize, colored, cprint


@pytest.fixture(autouse=True)
def _clear_can_colorize_cache():
    can_colorize.cache_clear()
    yield
    can_colorize.cache_clear()


# ---------------------------------------------------------------- colors


@pytest.mark.parametrize(
    "name,code",
    sorted(COLORS.items()),
)
def test_every_named_color(name, code):
    assert colored("x", name, force_color=True) == f"\x1b[{code}mx\x1b[0m"


@pytest.mark.parametrize(
    "name,code",
    sorted(HIGHLIGHTS.items()),
)
def test_every_named_highlight(name, code):
    assert colored("x", on_color=name, force_color=True) == f"\x1b[{code}mx\x1b[0m"


@pytest.mark.parametrize(
    "name,code",
    sorted(ATTRIBUTES.items()),
)
def test_every_attribute(name, code):
    assert colored("x", attrs=[name], force_color=True) == f"\x1b[{code}mx\x1b[0m"


def test_grey_is_black_alias():
    assert COLORS["grey"] == COLORS["black"] == 30
    assert HIGHLIGHTS["on_grey"] == HIGHLIGHTS["on_black"] == 40
    assert colored("x", "grey", force_color=True) == colored(
        "x", "black", force_color=True
    )


def test_code_order_is_attrs_then_color_then_highlight():
    # Regardless of argument order, attrs come first, then colour, then highlight.
    assert (
        colored("x", "red", "on_blue", ["bold"], force_color=True)
        == "\x1b[1;31;44mx\x1b[0m"
    )
    assert (
        colored("x", "red", "on_blue", ["bold", "underline"], force_color=True)
        == "\x1b[1;4;31;44mx\x1b[0m"
    )


def test_multiple_attrs_keep_given_order():
    assert (
        colored("x", attrs=["strike", "bold"], force_color=True) == "\x1b[9;1mx\x1b[0m"
    )


def test_no_codes_still_appends_reset_when_enabled():
    assert colored("hi", force_color=True) == "hi\x1b[0m"
    assert colored("hi", attrs=[], force_color=True) == "hi\x1b[0m"


def test_non_string_text_is_stringified():
    assert colored(123, "green", force_color=True) == "\x1b[32m123\x1b[0m"
    assert colored(None, force_color=True) == "None\x1b[0m"
    assert colored(3.5, "red", force_color=True) == "\x1b[31m3.5\x1b[0m"


def test_empty_text():
    assert colored("", "red", force_color=True) == "\x1b[31m\x1b[0m"
    assert colored("", force_color=True) == "\x1b[0m"


def test_unknown_color_raises_key_error():
    with pytest.raises(KeyError):
        colored("x", "orange", force_color=True)


def test_unknown_highlight_raises_key_error():
    with pytest.raises(KeyError):
        colored("x", on_color="on_orange", force_color=True)


def test_unknown_attribute_raises_key_error():
    with pytest.raises(KeyError):
        colored("x", attrs=["sparkle"], force_color=True)


def test_one_bad_attribute_aborts_whole_call():
    # The failing lookup happens before any output is produced.
    with pytest.raises(KeyError):
        colored("x", "red", attrs=["bold", "nope"], force_color=True)


# ---------------------------------------------------------------- RGB


@pytest.mark.parametrize(
    "rgb,expected",
    [
        ((255, 0, 0), "\x1b[38;2;255;0;0mx\x1b[0m"),
        ((0, 0, 0), "\x1b[38;2;0;0;0mx\x1b[0m"),
        ((255, 255, 255), "\x1b[38;2;255;255;255mx\x1b[0m"),
        ((12, 34, 56), "\x1b[38;2;12;34;56mx\x1b[0m"),
    ],
)
def test_rgb_foreground(rgb, expected):
    assert colored("x", rgb, force_color=True) == expected


@pytest.mark.parametrize(
    "rgb,expected",
    [
        ((255, 0, 0), "\x1b[48;2;255;0;0mx\x1b[0m"),
        ((0, 255, 128), "\x1b[48;2;0;255;128mx\x1b[0m"),
    ],
)
def test_rgb_background(rgb, expected):
    assert colored("x", on_color=rgb, force_color=True) == expected


def test_rgb_foreground_and_background_together():
    assert colored("x", (255, 0, 128), (0, 255, 0), force_color=True) == (
        "\x1b[38;2;255;0;128;48;2;0;255;0mx\x1b[0m"
    )


def test_rgb_mixed_with_named_and_attrs():
    assert colored("x", (10, 20, 30), "on_red", ["bold"], force_color=True) == (
        "\x1b[1;38;2;10;20;30;41mx\x1b[0m"
    )


@pytest.mark.parametrize(
    "bad",
    [(256, 0, 0), (-1, 0, 0), (0, 300, 0), (1, 2), (1, 2, 3, 4), ()],
)
def test_invalid_rgb_raises_value_error(bad):
    with pytest.raises(ValueError):
        colored("x", bad, force_color=True)
    with pytest.raises(ValueError):
        colored("x", on_color=bad, force_color=True)


# ------------------------------------------------------- enable / disable


def test_no_color_kwarg_wins_over_force_color_kwarg():
    # no_color is checked first in can_colorize.
    assert colored("x", "red", no_color=True, force_color=True) == "x"


def test_force_color_kwarg_overrides_no_color_env(monkeypatch):
    monkeypatch.setenv("NO_COLOR", "1")
    assert colored("x", "red", force_color=True) == "\x1b[31mx\x1b[0m"


def test_no_color_kwarg_overrides_force_color_env(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert colored("x", "red", no_color=True) == "x"


@pytest.mark.parametrize("var", ["NO_COLOR", "ANSI_COLORS_DISABLED"])
def test_disable_env_vars(monkeypatch, var):
    monkeypatch.setenv(var, "1")
    assert can_colorize() is False
    assert colored("x", "red") == "x"


def test_force_color_env_enables(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert can_colorize() is True


def test_dumb_terminal_disables(monkeypatch):
    monkeypatch.setenv("TERM", "dumb")
    assert can_colorize() is False


def test_can_colorize_caches_no_arg_calls(monkeypatch):
    # First call caches False; changing the env afterwards does not
    # change the cached answer until cache_clear().
    monkeypatch.setenv("NO_COLOR", "1")
    assert can_colorize() is False
    monkeypatch.delenv("NO_COLOR")
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert can_colorize() is False  # stale, cached
    can_colorize.cache_clear()
    assert can_colorize() is True


def test_explicit_kwargs_are_not_affected_by_cache(monkeypatch):
    monkeypatch.setenv("NO_COLOR", "1")
    assert can_colorize(no_color=True) is False
    assert can_colorize(force_color=True) is True


def test_colored_without_overrides_follows_env(monkeypatch):
    monkeypatch.setenv("FORCE_COLOR", "1")
    assert colored("x", "red") == "\x1b[31mx\x1b[0m"
    monkeypatch.delenv("FORCE_COLOR")
    can_colorize.cache_clear()
    monkeypatch.setenv("NO_COLOR", "1")
    assert colored("x", "red") == "x"


# ---------------------------------------------------------------- cprint


def test_cprint_writes_colored_line(capsys):
    cprint("hello", "green", force_color=True)
    assert capsys.readouterr().out == "\x1b[32mhello\x1b[0m\n"


def test_cprint_plain_when_disabled(capsys):
    cprint("hello", "green", no_color=True)
    assert capsys.readouterr().out == "hello\n"


def test_cprint_forwards_print_kwargs(capsys):
    cprint("a", "red", force_color=True, end="!")
    assert capsys.readouterr().out == "\x1b[31ma\x1b[0m!"
    cprint("b", force_color=True, file=__import__("sys").stdout)
    assert capsys.readouterr().out == "b\x1b[0m\n"


def test_cprint_with_attrs_and_highlight(capsys):
    cprint("x", "cyan", "on_magenta", ["underline"], force_color=True)
    assert capsys.readouterr().out == "\x1b[4;36;45mx\x1b[0m\n"
