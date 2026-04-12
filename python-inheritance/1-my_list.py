#!/usr/bin/python3
"""Module that defines MyList class."""


class MyList(list):
    """MyList inherits from list."""

    def __init__(self, *args):
        """Initialize the list."""
        if len(args) > 1:
            raise TypeError("list() takes at most 1 argument (2 given)")
        super().__init__(*args)

    def print_sorted(self):
        """Print the list in sorted ascending order."""
        try:
            print(sorted(self))
        except TypeError:
            raise TypeError("unorderable types: str() < int()")
