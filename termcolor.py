# coding: utf-8
# Copyright (c) 2008-2011 Volvox Development Team
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Author: Konstantin Lepa <konstantin.lepa@gmail.com>

"""ANSII Color formatting for output in terminal."""

import os


__ALL__ = [ 'colored' ]

VERSION = (1, 0, 1)

ATTRIBUTES = dict(
        list(zip([
            'bold',
            'dark',
            '',
            'underline',
            'blink',
            '',
            'reverse',
            'concealed'
            ],
            list(range(1, 9))
            ))
        )
del ATTRIBUTES['']


HIGHLIGHTS = dict(
        list(zip([
            'on_grey',
            'on_red',
            'on_green',
            'on_yellow',
            'on_blue',
            'on_magenta',
            'on_cyan',
            'on_white'
            ],
            list(range(40, 48))
            ))
        )


COLORS = dict(
        list(zip([
            'grey',
            'red',
            'green',
            'yellow',
            'blue',
            'magenta',
            'cyan',
            'white',
            ],
            list(range(30, 38))
            ))
        )


RESET = '\033[0m'


def colored(text, color=None, on_color=None, attrs=None):
    """Colorize text.

    Available text colors:
        red, green, yellow, blue, magenta, cyan, white.

    Available text highlights:
        on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed.

    Example:
        colored('Hello, World!', 'red', 'on_grey', ['blue', 'blink'])
        colored('Hello, World!', 'green')
    """
    if os.getenv('ANSI_COLORS_DISABLED') is None:
        fmt_str = '\033[%dm%s'
        if color is not None:
            text = fmt_str % (COLORS[color], text)

        if on_color is not None:
            text = fmt_str % (HIGHLIGHTS[on_color], text)

        if attrs is not None:
            for attr in attrs:
                text = fmt_str % (ATTRIBUTES[attr], text)

        text += RESET
    return text


if __name__ == '__main__':
    print(('Current terminal type: ', os.getenv('TERM')))
    print('Test basic colors:')
    print((colored('Grey color', 'grey')))
    print((colored('Red color', 'red')))
    print((colored('Green color', 'green')))
    print((colored('Yellow color', 'yellow')))
    print((colored('Blue color', 'blue')))
    print((colored('Magenta color', 'magenta')))
    print((colored('Cyan color', 'cyan')))
    print((colored('White color', 'white')))
    print(('-' * 78))

    print('Test highlights:')
    print((colored('On grey color', on_color='on_grey')))
    print((colored('On red color', on_color='on_red')))
    print((colored('On green color', on_color='on_green')))
    print((colored('On yellow color', on_color='on_yellow')))
    print((colored('On blue color', on_color='on_blue')))
    print((colored('On magenta color', on_color='on_magenta')))
    print((colored('On cyan color', on_color='on_cyan')))
    print((colored('On white color', color='grey', on_color='on_white')))
    print(('-' * 78))

    print('Test attributes:')
    print((colored('Bold grey color', 'grey', attrs=['bold'])))
    print((colored('Dark red color', 'red', attrs=['dark'])))
    print((colored('Underline green color', 'green', attrs=['underline'])))
    print((colored('Blink yellow color', 'yellow', attrs=['blink'])))
    print((colored('Reversed blue color', 'blue', attrs=['reverse'])))
    print((colored('Concealed Magenta color', 'magenta', attrs=['concealed'])))
    print((colored('Bold underline reverse cyan color', 'cyan',
            attrs=['bold', 'underline', 'reverse'])))
    print((colored('Dark blink concealed white color', 'white',
            attrs=['dark', 'blink', 'concealed'])))
    print(('-' * 78))

    print('Test mixing:')
    print((colored('Underline red on grey color', 'red', 'on_grey',
            ['underline'])))
    print((colored('Reversed green on red color', 'green', 'on_red', ['reverse'])))

