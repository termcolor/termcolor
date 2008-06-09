# Copyright (C) 2008 Konstantin Lepa <konstantin.lepa@gmail.com>.
#
# This file is part of termcolor.
#
# termcolor is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 3, or (at your option) any later
# version.
#
# termcolor is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License
# along with termcolor.  If not, see <http://www.gnu.org/licenses/>.

"""ANSII Color formatting for output in terminal."""

import os


__ALL__ = [ 'colored' ]


attributes = dict(
        zip([
            'bold',
            'dark',
            '',
            'underline',
            'blink',
            '',
            'reverse',
            'concealed'
            ],
            range(1, 9)
            )
        )
del attributes['']


highlights = dict(
        zip([
            'on_grey',
            'on_red',
            'on_green',
            'on_yellow',
            'on_blue',
            'on_magenta',
            'on_cyan',
            'on_white'
            ],
            range(40, 48)
            )
        )


colors = dict(
        zip([
            'grey',
            'red',
            'green',
            'yellow',
            'blue',
            'magenta',
            'cyan',
            'white',
            ],
            range(30, 38)
            )
        )


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
        fmt_str = '\033[1;%dm%s'
        if color is not None:
            text = fmt_str % (colors[color], text)

        if on_color is not None:
            text = fmt_str % (highlights[on_color], text)

        if attrs is not None:
            for attr in attrs:
                text = fmt_str % (attributes[attr], text)

        reset = '\033[1;m'
        text += reset

    return text


if __name__ == '__main__':
    print 'Current terminal type: ', os.getenv('TERM')
    print 'Test basic colors:'
    print colored('Grey color', 'grey')
    print colored('Red color', 'red')
    print colored('Green color', 'green')
    print colored('Yellow color', 'yellow')
    print colored('Blue color', 'blue')
    print colored('Magenta color', 'magenta')
    print colored('Cyan color', 'cyan')
    print colored('White color', 'white')
    print '-' * 78

    print 'Test highlights:'
    print colored('On grey color', on_color='on_grey')
    print colored('On red color', on_color='on_red')
    print colored('On green color', on_color='on_green')
    print colored('On yellow color', on_color='on_yellow')
    print colored('On blue color', on_color='on_blue')
    print colored('On magenta color', on_color='on_magenta')
    print colored('On cyan color', on_color='on_cyan')
    print colored('On white color', color='grey', on_color='on_white')
    print '-' * 78

    print 'Test attributes:'
    print colored('Bold grey color', 'grey', attrs=['bold'])
    print colored('Dark red color', 'red', attrs=['dark'])
    print colored('Underline green color', 'green', attrs=['underline'])
    print colored('Blink yellow color', 'yellow', attrs=['blink'])
    print colored('Reversed blue color', 'blue', attrs=['reverse'])
    print colored('Concealed Magenta color', 'magenta', attrs=['concealed'])
    print colored('Bold underline reverse cyan color', 'cyan',
            attrs=['bold', 'underline', 'reverse'])
    print colored('Dark blink concealed white color', 'white',
            attrs=['dark', 'blink', 'concealed'])
    print '-' * 78

    print 'Test mixing:'
    print colored('Underline red on grey color', 'red', 'on_grey',
            ['underline'])
    print colored('Reversed green on red color', 'green', 'on_red', ['reverse'])

