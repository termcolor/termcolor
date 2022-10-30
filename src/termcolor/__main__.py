from __future__ import annotations

import os

from termcolor import cprint

if __name__ == "__main__":
    print(f"Current terminal type: {os.getenv('TERM')}")
    print("Test basic colors:")
    cprint("Grey color", "grey")
    cprint("Red color", "red")
    cprint("Green color", "green")
    cprint("Yellow color", "yellow")
    cprint("Blue color", "blue")
    cprint("Magenta color", "magenta")
    cprint("Cyan color", "cyan")
    cprint("White color", "white")
    print("-" * 78)

    print("Test highlights:")
    cprint("On grey color", on_color="on_grey")
    cprint("On red color", on_color="on_red")
    cprint("On green color", on_color="on_green")
    cprint("On yellow color", on_color="on_yellow")
    cprint("On blue color", on_color="on_blue")
    cprint("On magenta color", on_color="on_magenta")
    cprint("On cyan color", on_color="on_cyan")
    cprint("On white color", color="grey", on_color="on_white")
    print("-" * 78)

    print("Test attributes:")
    cprint("Bold grey color", "grey", attrs=["bold"])
    cprint("Dark red color", "red", attrs=["dark"])
    cprint("Underline green color", "green", attrs=["underline"])
    cprint("Blink yellow color", "yellow", attrs=["blink"])
    cprint("Reversed blue color", "blue", attrs=["reverse"])
    cprint("Concealed Magenta color", "magenta", attrs=["concealed"])
    cprint(
        "Bold underline reverse cyan color",
        "cyan",
        attrs=["bold", "underline", "reverse"],
    )
    cprint(
        "Dark blink concealed white color",
        "white",
        attrs=["dark", "blink", "concealed"],
    )
    print("-" * 78)

    print("Test mixing:")
    cprint("Underline red on grey color", "red", "on_grey", ["underline"])
    cprint("Reversed green on red color", "green", "on_red", ["reverse"])
