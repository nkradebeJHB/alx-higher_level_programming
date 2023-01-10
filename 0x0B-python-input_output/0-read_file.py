#!/usr/bin/python3

def read_file(filename=""):
    """A function that reads a text file and prints it"""
    with open(filename, "r", encoding="UTF-8") as f:
        text = f.read()
        print(text, end="")
