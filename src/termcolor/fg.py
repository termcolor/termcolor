"""Foreground colour codes: from termcolor.fg import red"""

from __future__ import annotations

from termcolor.termcolor import _RGB_FORE_FMT, COLORS, _check_rgb, _Code

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

_OFF = "\033[39m"


def _fg(name: str) -> _Code:
    return _Code(f"\033[{COLORS[name]}m", _OFF)


def rgb(r: int, g: int, b: int) -> _Code:
    """Foreground colour from 0-255 RGB ints."""
    _check_rgb((r, g, b))
    return _Code(f"\033[{_RGB_FORE_FMT % (r, g, b)}m", _OFF)


black = _fg("black")
grey = _fg("grey")
red = _fg("red")
green = _fg("green")
yellow = _fg("yellow")
blue = _fg("blue")
magenta = _fg("magenta")
cyan = _fg("cyan")
light_grey = _fg("light_grey")
dark_grey = _fg("dark_grey")
light_red = _fg("light_red")
light_green = _fg("light_green")
light_yellow = _fg("light_yellow")
light_blue = _fg("light_blue")
light_magenta = _fg("light_magenta")
light_cyan = _fg("light_cyan")
white = _fg("white")
