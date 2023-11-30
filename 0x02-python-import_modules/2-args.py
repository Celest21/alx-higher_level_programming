#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    plural_suffix = 's' if argc != 1 else ''
    print("Number of argument{}: {}".format(plural_suffix, argc), end="")

    if argc == 0:
        print(".")
    else:
        print(":")
        for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))
