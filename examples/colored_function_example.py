#                                         #
# EXAMPLE USAGE OF THE COLORED() FUNTCION #
#                BY MILESWK               #
#                    :)                   #
#                                         #
from __future__ import annotations

from termcolor import colored  # Import the module

# Syntax for "colored()" function:
# colored(text, text_color, on_color)

# This is our text normally:
normal_text = "Hello! Please color me!"

# Print the unformatted text:
print(normal_text)  # >>> Hello! Please color me!

# New variable alert! This one is coloring the text to blue:
colored_text = colored(normal_text, "blue")

# Let's print the colored version:
print(colored_text)  # >>> (blue) Hello! Please color me!

# Now let's change the color again:
colored_text = colored(normal_text, "blue", "on_white")

# Let's print that...
print(colored_text)  # >>> (blue with a white background) Hello! Please color me!
