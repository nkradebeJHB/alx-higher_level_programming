#!/usr/bin/python3
def add_arg(argv):
    count = len(argv) - 1
    if count == 0:
        print("{:d}".format(count))
        return
    else:
        i = 1
        add = 0
        while i <= count:
            add += int(argv[i])
            i += 1
        print("{:d}".format(add))

if __name__ == "__main__":
    import sys
    add_arg(sys.argv)
