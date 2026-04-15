#!/usr/bin/python3
"""Salam"""


def append_write(filename="", text=""):
    """Izah"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
