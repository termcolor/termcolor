import pytest

from termcolor import ATTRIBUTES, COLORS, HIGHLIGHTS, colored, cprint

ALL_COLORS = list(COLORS) + [None]
ALL_HIGHLIGHTS = list(HIGHLIGHTS) + [None]
ALL_ATTRIBUTES = list(ATTRIBUTES) + [None]


def test_basic():
    assert colored("text") == "text\x1b[0m"


def test_sanity():
    for color in ALL_COLORS:
        for highlight in ALL_HIGHLIGHTS:
            for attribute in ALL_ATTRIBUTES:
                attrs = None if attribute is None else [attribute]
                colored("text", color, highlight, attrs)
                cprint("text", color, highlight, attrs)


def assert_cprint(
    capsys, expected, text, color=None, on_color=None, attrs=None, **kwargs
):
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
def test_color(capsys, color, expected):
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
def test_on_color(capsys, on_color, expected):
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
def test_attrs(capsys, attr, expected):
    assert colored("text", attrs=[attr]) == expected
    assert_cprint(capsys, expected, "text", attrs=[attr])
