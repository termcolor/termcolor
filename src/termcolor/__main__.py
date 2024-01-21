from __future__ import annotations

import os

from termcolor import cprint

if __name__ == "__main__":
    print(f"Current terminal type: {os.getenv('TERM')}")
    print("Test basic colors:")
    cprint("Black color", "black")
    cprint("Red color", "red")
    cprint("Green color", "green")
    cprint("Yellow color", "yellow")
    cprint("Blue color", "blue")
    cprint("Magenta color", "magenta")
    cprint("Cyan color", "cyan")
    cprint("White color", "white")
    cprint("Light grey color", "light_grey")
    cprint("Dark grey color", "dark_grey")
    cprint("Light red color", "light_red")
    cprint("Light green color", "light_green")
    cprint("Light yellow color", "light_yellow")
    cprint("Light blue color", "light_blue")
    cprint("Light magenta color", "light_magenta")
    cprint("Light cyan color", "light_cyan")
    print("-" * 78)

    print("Test highlights:")
    cprint("On black color", on_color="black")
    cprint("On red color", on_color="red")
    cprint("On green color", on_color="green")
    cprint("On yellow color", on_color="yellow")
    cprint("On blue color", on_color="blue")
    cprint("On magenta color", on_color="magenta")
    cprint("On cyan color", on_color="cyan")
    cprint("On white color", color="black", on_color="white")
    cprint("On light grey color", on_color="light_grey")
    cprint("On dark grey color", on_color="dark_grey")
    cprint("On light red color", on_color="light_red")
    cprint("On light green color", on_color="light_green")
    cprint("On light yellow color", on_color="light_yellow")
    cprint("On light blue color", on_color="light_blue")
    cprint("On light magenta color", on_color="light_magenta")
    cprint("On light cyan color", on_color="light_cyan")
    print("-" * 78)

    print("Test attributes:")
    cprint("Bold black color", "black", attrs=["bold"])
    cprint("Dark red color", "red", attrs=["dark"])
    cprint("Underline green color", "green", attrs=["underline"])
    cprint("Blink yellow color", "yellow", attrs=["blink"])
    cprint("Reversed blue color", "blue", attrs=["reverse"])
    cprint("Concealed magenta color", "magenta", attrs=["concealed"])
    cprint("Strike red color", "red", attrs=["strike"])
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
    cprint("Underline red on black color", "red", "black", ["underline"])
    cprint("Reversed green on red color", "green", "red", ["reverse"])
