#!/usr/bin/env python3
"""
Module for 9-element_length.py
"""

import typing


def element_length(
        lst: typing.Iterable[typing.Sequence]
        ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Element length function"""
    return [(i, len(i)) for i in lst]
