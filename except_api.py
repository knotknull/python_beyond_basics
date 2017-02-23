#!/usr/bin/env python3.5
""" keypress - A module for detecting a single keypres."""

# The following code will attemp to import a windows specific module and
# if that fails an ImportError will be reaised and caught at which point
# unix / linux specific modules will be import.  If successful getkey is
# for defined unix / linux otherwise tty module will throw an ImportError
# which is NOT caught and sent back to the caller.

try:
    import msvcrt

    def getkey():
        """Wait for a keypress and return a signle character string."""
        return msvcrt.getch()

except ImportError as e:

    import sys
    import tty
    import termios

    print("ImportError caught e = {}".format(e))

    def getkey():
        """Wait for a keypress and returna signle character string."""
        fd = sys.stdin.fileno()
        original_attr = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, original_attr)
            return ch

    # If either of the Unix-specific tty or termios are not found,
    # we allow for the ImportError to propogate from here

getkey()
