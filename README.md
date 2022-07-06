# termcolor

[![PyPI version](https://img.shields.io/pypi/v/termcolor.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/termcolor)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/termcolor.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/termcolor)
[![PyPI downloads](https://img.shields.io/pypi/dm/termcolor.svg)](https://pypistats.org/packages/termcolor)
[![GitHub Actions status](https://github.com/termcolor/termcolor/workflows/Test/badge.svg)](https://github.com/termcolor/termcolor/actions)
[![Codecov](https://codecov.io/gh/termcolor/termcolor/branch/main/graph/badge.svg)](https://codecov.io/gh/termcolor/termcolor)
[![Licence](https://img.shields.io/github/license/termcolor/termcolor.svg)](COPYING.txt)
[![Code style: Black](https://img.shields.io/badge/code%20style-Black-000000.svg)](https://github.com/psf/black)

## Example

```python
import sys

from termcolor import colored, cprint

text = colored("Hello, World!", "red", attrs=["reverse", "blink"])
print(text)
cprint("Hello, World!", "green", "on_red")

print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")
print_red_on_cyan("Hello, World!")
print_red_on_cyan("Hello, Universe!")

for i in range(10):
    cprint(i, "magenta", end=" ")

cprint("Attention!", "red", attrs=["bold"], file=sys.stderr)
```

## Text properties

Text colors:

- grey
- red
- green
- yellow
- blue
- magenta
- cyan
- white

Text highlights:

- on_grey
- on_red
- on_green
- on_yellow
- on_blue
- on_magenta
- on_cyan
- on_white

Attributes:

- bold
- dark
- underline
- blink
- reverse
- concealed

## Terminal properties

| Terminal     | bold    | dark | underline | blink      | reverse | concealed |
| ------------ | ------- | ---- | --------- | ---------- | ------- | --------- |
| xterm        | yes     | no   | yes       | bold       | yes     | yes       |
| linux        | yes     | yes  | bold      | yes        | yes     | no        |
| rxvt         | yes     | no   | yes       | bold/black | yes     | no        |
| dtterm       | yes     | yes  | yes       | reverse    | yes     | yes       |
| teraterm     | reverse | no   | yes       | rev/red    | yes     | no        |
| aixterm      | normal  | no   | yes       | no         | yes     | yes       |
| PuTTY        | color   | no   | yes       | no         | yes     | no        |
| Windows      | no      | no   | no        | no         | yes     | no        |
| Cygwin SSH   | yes     | no   | color     | color      | color   | yes       |
| Mac Terminal | yes     | no   | yes       | yes        | yes     | yes       |
