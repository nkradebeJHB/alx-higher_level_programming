#!/usr/bin/python3

def print_arg(argv):
    """Print the number of and list of arguments."""
    count = len(argv) - 1
    if count == 0:
        print("{:d} argument.".format(count))
        return
    else:
        if count == 1:
            print("{:d} argument:".format(count))
        else:
            print("{:d} arguments:".format(count))
        i = 1
        while i <= count:
            print("{:d}: {:is}".format(i, argv[i]))
            i += 1

if __name__ == "__main__":
    import sys

    print_arg(sys.argv)
