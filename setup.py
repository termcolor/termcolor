#!/usr/bin/env python
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


from distutils.core import setup

long_desc="""
Available text colors
---------------------
    red, green, yellow, blue, magenta, cyan, white.

Available text highlights
-------------------------
    on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.

Available attributes
--------------------
    bold, dark, underline, blink, reverse, concealed.

Example
-------
::

    from termcolor import colored

    print colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
    print colored('Hello, World!', 'green', 'on_red')


Terminal properties
-------------------
============ ======= ==== ===== ========== ======= =======
Terminal     bold    dark under blink      reverse conceal
------------ ------- ---- ----- ---------- ------- -------
xterm        yes     no   yes   bold       yes     yes
linux        yes     yes  bold  yes        yes     no
rxvt         yes     no   yes   bold/black yes     no
dtterm       yes     yes  yes   reverse    yes     yes
teraterm     reverse no   yes   rev/red    yes     no
aixterm      normal  no   yes   no         yes     yes
PuTTY        color   no   yes   no         yes     no
Windows      no      no   no    no         yes     no
Cygwin SSH   yes     no   color color      color   yes
Mac Terminal yes     no   yes   yes        yes     yes
============ ======= ==== ===== ========== ======= =======

"""

setup(name='termcolor',
      version='0.1',
      description='ANSII Color formatting for output in terminal.',
      long_description=long_desc,
      author='Konstantin Lepa',
      license='GPL',
      author_email='konstantin.lepa@gmail.com',
      url='http://pypi.python.org/pypi/termcolor',
      py_modules=['termcolor'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Terminals'
          ]
      )
