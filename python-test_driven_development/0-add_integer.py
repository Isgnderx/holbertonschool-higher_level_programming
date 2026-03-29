#!/usr/bin/python3
"""This module provides a function that adds two integers."""


def add_integer(a, b=98):
    """Add two integers after casting float arguments to integers."""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if isinstance(a, float):
        a = int(a)

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(b, float):
        b = int(b)

    return a + b
