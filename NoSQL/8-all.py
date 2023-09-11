#!/usr/bin/env python3
"""
Module for task 8-all.py
"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    if mongo_collection is None:
        return []
    return mongo_collection.find()
