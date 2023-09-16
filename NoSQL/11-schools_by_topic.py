#!/usr/bin/env python3
"""
Returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """Return school by topic"""

    schools = mongo_collection.find({
        "topics": {
            "$in": [topic]
        }
    })
    return schools
