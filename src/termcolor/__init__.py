"""ANSI color formatting for output in terminal."""
from __future__ import annotations

from termcolor.termcolor import ATTRIBUTES, HIGHLIGHTS, COLORS, RESET, colored, cprint

__all__ = [
    "ATTRIBUTES",
    "COLORS",
    "HIGHLIGHTS",
    "RESET",
    "colored",
    "cprint",
]
