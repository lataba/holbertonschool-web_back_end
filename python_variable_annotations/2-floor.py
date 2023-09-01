#!/usr/bin/env python3
"""
Module for 2-floor.py
"""


def floor(n: float) -> int:
    """
    Function that returns the floor of a number
    """
    if n > 0:
        return int(n)
    else:
        return int(n) - 1
