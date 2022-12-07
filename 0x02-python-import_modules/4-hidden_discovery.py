#!/usr/bin/python3
import hidden_4

def discover():
    strings = dir(hidden_4)
    for i in strings:
        if i[:2] != '__':
            print("{:s}".format(i))

if __name__ == "__main__":
    discover()
