#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    addition = 0
    for i in range(len(argv) - 1):
        addition += int(argv[i+1])
    print("{}".format(addition))
