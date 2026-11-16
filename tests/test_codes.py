"""Tests for the Code objects: termcolor.fg, .bg, .attrs and the top level"""

from __future__ import annotations

import copy
import pickle

import pytest

import termcolor
from termcolor import (
    ATTRIBUTES,
    COLORS,
    HIGHLIGHTS,
    RESET,
    attrs,
    bg,
    blue,
    bold,
    can_colorize,
    fg,
    italic,
    on_blue,
    red,
    reset,
)
from termcolor.termcolor import _Code, _Escape

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Generator


@pytest.fixture(autouse=True)
def _force_color(monkeypatch: pytest.MonkeyPatch) -> Generator[None]:
    # Code objects decide whether colour is enabled when used, via the cache.
    for var in ("ANSI_COLORS_DISABLED", "NO_COLOR", "FORCE_COLOR"):
        monkeypatch.delenv(var, raising=False)
    monkeypatch.setenv("FORCE_COLOR", "1")
    can_colorize.cache_clear()
    yield
    can_colorize.cache_clear()


@pytest.fixture
def _no_color(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("NO_COLOR", "1")  # Takes precedence over FORCE_COLOR


def test_string_form() -> None:
    assert f"{red}{on_blue}Hi{reset}" == "\x1b[31m\x1b[44mHi\x1b[0m"
    assert str(fg.red) == "\x1b[31m"
    assert f"{fg.red!s:>6}" == " \x1b[31m"
    with pytest.raises(TypeError, match=r"unsupported format string"):
        f"{fg.red:>6}"
    assert fg.red + "Hi" == "\x1b[31mHi"
    assert "Hi" + fg.red == "Hi\x1b[31m"
    assert fg.red + on_blue == "\x1b[31m\x1b[44m"
    with pytest.raises(TypeError):
        fg.red + 1
    with pytest.raises(TypeError):
        1 + fg.red


def test_call_form_nests() -> None:
    # Only the inner style is switched off, so the outer one continues
    assert italic(f"{red('a')} b") == "\x1b[3m\x1b[31ma\x1b[39m b\x1b[23m"
    assert bold(red("Hi")) == "\x1b[1m\x1b[31mHi\x1b[39m\x1b[22m"


@pytest.mark.parametrize("name", COLORS)
def test_fg(name: str) -> None:
    code = getattr(fg, name)
    assert code is getattr(termcolor, name)
    assert str(code) == f"\x1b[{COLORS[name]}m"
    assert code("Hi") == f"\x1b[{COLORS[name]}mHi\x1b[39m"


@pytest.mark.parametrize("name", HIGHLIGHTS)
def test_bg(name: str) -> None:
    code = getattr(bg, name.removeprefix("on_"))
    assert code is getattr(termcolor, name)
    assert str(code) == f"\x1b[{HIGHLIGHTS[name]}m"
    assert code("Hi") == f"\x1b[{HIGHLIGHTS[name]}mHi\x1b[49m"


@pytest.mark.parametrize(
    "name, off",
    [
        ("bold", 22),
        ("dark", 22),
        ("italic", 23),
        ("underline", 24),
        ("blink", 25),
        ("reverse", 27),
        ("concealed", 28),
        ("strike", 29),
    ],
)
def test_attrs(name: str, off: int) -> None:
    code = getattr(attrs, name)
    assert code is getattr(termcolor, name)
    assert str(code) == f"\x1b[{ATTRIBUTES[name]}m"
    assert code("Hi") == f"\x1b[{ATTRIBUTES[name]}mHi\x1b[{off}m"


def test_rgb() -> None:
    assert str(fg.rgb(1, 2, 3)) == "\x1b[38;2;1;2;3m"
    assert fg.rgb(1, 2, 3)("Hi") == "\x1b[38;2;1;2;3mHi\x1b[39m"
    assert str(bg.rgb(1, 2, 3)) == "\x1b[48;2;1;2;3m"
    assert bg.rgb(1, 2, 3)("Hi") == "\x1b[48;2;1;2;3mHi\x1b[49m"


@pytest.mark.parametrize("r, g, b", [(256, 0, 0), (0, -1, 0)])
def test_rgb_invalid(r: int, g: int, b: int) -> None:
    with pytest.raises(ValueError, match="Expected a tuple of 3 ints in range 0-255"):
        fg.rgb(r, g, b)
    with pytest.raises(ValueError, match="Expected a tuple of 3 ints in range 0-255"):
        bg.rgb(r, g, b)


def test_reset() -> None:
    assert str(reset) == RESET == "\x1b[0m"
    assert isinstance(reset, _Escape)
    assert not isinstance(reset, _Code)
    assert not callable(reset)
    assert reset == _Escape(RESET)
    assert hash(reset) == hash(_Escape(RESET))
    assert reset != _Code(RESET, "")
    assert repr(reset) == "_Escape('\\x1b[0m')"


def test_overrides_when_enabled() -> None:
    assert red("Hi", no_color=True) == "Hi"
    assert red("Hi", force_color=True) == "\x1b[31mHi\x1b[39m"


@pytest.mark.usefixtures("_no_color")
def test_disabled() -> None:
    assert str(red) == ""
    assert str(reset) == ""
    assert f"{red}Hi{reset}" == "Hi"
    assert red + "Hi" == "Hi"
    assert red("Hi") == "Hi"
    assert bold(red("Hi")) == "Hi"
    assert str(fg.rgb(1, 2, 3)) == ""
    # Codes stay distinct when disabled
    assert red != blue
    assert red
    # Overrides still apply
    assert red("Hi", force_color=True) == "\x1b[31mHi\x1b[39m"
    assert red("Hi", no_color=True) == "Hi"


def test_eq_hash() -> None:
    assert fg.red == _Code("\x1b[31m", "\x1b[39m")
    assert fg.red != fg.blue
    assert fg.red != "\x1b[31m"
    assert hash(fg.red) == hash(_Code("\x1b[31m", "\x1b[39m"))
    assert len({fg.red, fg.blue, fg.red}) == 2
    assert fg.red


@pytest.mark.parametrize("fn", [copy.copy, copy.deepcopy])
def test_copy(fn: object) -> None:
    assert fn(fg.red) == fg.red  # type: ignore[operator]


def test_pickle() -> None:
    assert pickle.loads(pickle.dumps(fg.red)) == fg.red  # noqa: S301


def test_str_of_text_consistent() -> None:
    class Obj:
        def __str__(self) -> str:
            return "S"

        def __format__(self, spec: str) -> str:
            return "FMT"

    assert f"{Obj()}" != str(Obj())
    assert fg.red(Obj(), force_color=True) == "\x1b[31mS\x1b[39m"
    assert fg.red(Obj(), no_color=True) == "S"


def test_repr() -> None:
    assert repr(fg.red) == "_Code('\\x1b[31m', '\\x1b[39m')"
    assert repr(_Code("on", "off")) == "_Code('on', 'off')"


def test_all() -> None:
    assert set(fg.__all__) == {*COLORS, "rgb"}
    assert set(bg.__all__) == {name.removeprefix("on_") for name in HIGHLIGHTS} | {
        "rgb"
    }
    assert set(attrs.__all__) == set(ATTRIBUTES)
    assert {*COLORS, *HIGHLIGHTS, *ATTRIBUTES, "reset"} <= set(termcolor.__all__)
    for module in (fg, bg, attrs, termcolor):
        for name in module.__all__:
            assert hasattr(module, name), f"{module.__name__}.{name}"
