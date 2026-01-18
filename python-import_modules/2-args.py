#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv) - 1
    if count == 0:
        print("Number of arguments(s).")
    else:
        print("Number of arguments(s):".format())
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
