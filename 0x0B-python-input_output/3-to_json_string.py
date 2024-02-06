#!/usr/bin/python3
"""Defines a json_representation function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of my_obj."""
    return json.dumps(my_obj)
