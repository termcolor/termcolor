"""Background colour codes: from termcolor.bg import red"""

from __future__ import annotations

from termcolor.termcolor import _RGB_BACK_FMT, HIGHLIGHTS, _check_rgb, _Code

__all__ = [
    "black",
    "blue",
    "cyan",
    "dark_grey",
    "green",
    "grey",
    "light_blue",
    "light_cyan",
    "light_green",
    "light_grey",
    "light_magenta",
    "light_red",
    "light_yellow",
    "magenta",
    "red",
    "rgb",
    "white",
    "yellow",
]

_OFF = "\033[49m"


def _bg(name: str) -> _Code:
    return _Code(f"\033[{HIGHLIGHTS[f'on_{name}']}m", _OFF)


def rgb(r: int, g: int, b: int) -> _Code:
    """Background colour from 0-255 RGB ints."""
    _check_rgb((r, g, b))
    return _Code(f"\033[{_RGB_BACK_FMT % (r, g, b)}m", _OFF)


black = _bg("black")
grey = _bg("grey")
red = _bg("red")
green = _bg("green")
yellow = _bg("yellow")
blue = _bg("blue")
magenta = _bg("magenta")
cyan = _bg("cyan")
light_grey = _bg("light_grey")
dark_grey = _bg("dark_grey")
light_red = _bg("light_red")
light_green = _bg("light_green")
light_yellow = _bg("light_yellow")
light_blue = _bg("light_blue")
light_magenta = _bg("light_magenta")
light_cyan = _bg("light_cyan")
white = _bg("white")
