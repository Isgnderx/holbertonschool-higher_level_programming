#!/usr/bin/python3
"""Module that defines MyList class."""


class MyList(list):
    """MyList inherits from list and prints a sorted version."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
