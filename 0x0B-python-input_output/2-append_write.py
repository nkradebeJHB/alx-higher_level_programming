#!/urs/bin/python3


def append_write(filename="", text=""):
    """function that appends a string at the end of a text
    file and returns the number of charecters"""

    with    open(filename, 'a') as  f:
        return  f.write(text)
