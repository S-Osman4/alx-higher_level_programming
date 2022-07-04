#!/usr/bin/python3
"""Lookup method."""


def lookup(obj):
    """
    Args:
        obj: The list object.
    Return:
        The list of available attributes and methods of an object.
    """
    return dir(obj)
