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

import os
from distutils.core import setup


LONG_DESC = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()
CHANGES = open(os.path.join(os.path.dirname(__file__), 'CHANGES.txt')).read()
LONG_DESC += '\nCHANGES\n=======\n\n' + CHANGES


setup(name='termcolor',
      version='0.1.2',
      description='ANSII Color formatting for output in terminal.',
      long_description=LONG_DESC,
      author='Konstantin Lepa',
      license='GPL',
      author_email='konstantin.lepa@gmail.com',
      url='http://pypi.python.org/pypi/termcolor',
      py_modules=['termcolor'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Terminals'
          ]
      )
