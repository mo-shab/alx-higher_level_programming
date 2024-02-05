#!/usr/bin/python3
"""Module for class MyList"""


class MyList(list):
    """Class to print_sorted"""

    def print_sorted(self):
        """Methot that print sorted a list"""

        print(sorted(self))
