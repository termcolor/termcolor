Available text colors
---------------------
    grey, red, green, yellow, blue, magenta, cyan, white.

Available text highlights
-------------------------
    on_grey, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan,
    on_white.

Available attributes
--------------------
    bold, dark, underline, blink, reverse, concealed.

Example
-------
::

    from termcolor import colored

    print colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
    print colored('Hello, World!', 'green', 'on_red')

    red_on_cyan = lambda x: colored(x, 'red', 'on_cyan')
    print red_on_cyan('Hello, World!')
    print red_on_cyan('Hello, Universe!')


Terminal properties
-------------------
============ ======= ==== ========= ========== ======= =========
Terminal     bold    dark underline blink      reverse concealed
------------ ------- ---- --------- ---------- ------- ---------
xterm        yes     no   yes       bold       yes     yes
linux        yes     yes  bold      yes        yes     no
rxvt         yes     no   yes       bold/black yes     no
dtterm       yes     yes  yes       reverse    yes     yes
teraterm     reverse no   yes       rev/red    yes     no
aixterm      normal  no   yes       no         yes     yes
PuTTY        color   no   yes       no         yes     no
Windows      no      no   no        no         yes     no
Cygwin SSH   yes     no   color     color      color   yes
Mac Terminal yes     no   yes       yes        yes     yes
============ ======= ==== ========= ========== ======= =========

