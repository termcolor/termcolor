"""ANSI color formatting for output in terminal."""

from __future__ import annotations

__lazy_modules__ = {
    "termcolor",
    "termcolor.attrs",
    "termcolor.bg",
    "termcolor.fg",
    "termcolor.termcolor",
}

from termcolor import attrs, bg, fg
from termcolor.attrs import (
    blink,
    bold,
    concealed,
    dark,
    italic,
    reverse,
    strike,
    underline,
)
from termcolor.bg import black as on_black
from termcolor.bg import blue as on_blue
from termcolor.bg import cyan as on_cyan
from termcolor.bg import dark_grey as on_dark_grey
from termcolor.bg import green as on_green
from termcolor.bg import grey as on_grey
from termcolor.bg import light_blue as on_light_blue
from termcolor.bg import light_cyan as on_light_cyan
from termcolor.bg import light_green as on_light_green
from termcolor.bg import light_grey as on_light_grey
from termcolor.bg import light_magenta as on_light_magenta
from termcolor.bg import light_red as on_light_red
from termcolor.bg import light_yellow as on_light_yellow
from termcolor.bg import magenta as on_magenta
from termcolor.bg import red as on_red
from termcolor.bg import white as on_white
from termcolor.bg import yellow as on_yellow
from termcolor.fg import (
    black,
    blue,
    cyan,
    dark_grey,
    green,
    grey,
    light_blue,
    light_cyan,
    light_green,
    light_grey,
    light_magenta,
    light_red,
    light_yellow,
    magenta,
    red,
    white,
    yellow,
)
from termcolor.termcolor import (
    ATTRIBUTES,
    COLORS,
    HIGHLIGHTS,
    RESET,
    can_colorize,
    colored,
    cprint,
    reset,
)

__all__ = [
    "ATTRIBUTES",
    "COLORS",
    "HIGHLIGHTS",
    "RESET",
    "attrs",
    "bg",
    "black",
    "blink",
    "blue",
    "bold",
    "can_colorize",
    "colored",
    "concealed",
    "cprint",
    "cyan",
    "dark",
    "dark_grey",
    "fg",
    "green",
    "grey",
    "italic",
    "light_blue",
    "light_cyan",
    "light_green",
    "light_grey",
    "light_magenta",
    "light_red",
    "light_yellow",
    "magenta",
    "on_black",
    "on_blue",
    "on_cyan",
    "on_dark_grey",
    "on_green",
    "on_grey",
    "on_light_blue",
    "on_light_cyan",
    "on_light_green",
    "on_light_grey",
    "on_light_magenta",
    "on_light_red",
    "on_light_yellow",
    "on_magenta",
    "on_red",
    "on_white",
    "on_yellow",
    "red",
    "reset",
    "reverse",
    "strike",
    "underline",
    "white",
    "yellow",
]
