#!/usr/bin/python3


def read_file(filename=""):
    """A function that reads a text file and prints it"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
