"""Text attribute codes: from termcolor.attrs import bold"""

from __future__ import annotations

from termcolor.termcolor import ATTRIBUTES, _Code

__all__ = [
    "blink",
    "bold",
    "concealed",
    "dark",
    "italic",
    "reverse",
    "strike",
    "underline",
]

# Codes to switch off a single attribute. Bold and dark share one.
_OFF = {
    "bold": 22,
    "dark": 22,
    "italic": 23,
    "underline": 24,
    "blink": 25,
    "reverse": 27,
    "concealed": 28,
    "strike": 29,
}


def _attr(name: str) -> _Code:
    return _Code(f"\033[{ATTRIBUTES[name]}m", f"\033[{_OFF[name]}m")


bold = _attr("bold")
dark = _attr("dark")
italic = _attr("italic")
underline = _attr("underline")
blink = _attr("blink")
reverse = _attr("reverse")
concealed = _attr("concealed")
strike = _attr("strike")
