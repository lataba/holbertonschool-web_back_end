#!/usr/bin/env python3
"""
Inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """Insert into school collection"""

    document = mongo_collection.insert(kwargs)
    return document
