#!/usr/bin/python3
def _upper(c):
    if ord(c) in range(97, 123):
        return(ord(c) - 32)
    else:
        return(ord(c))


def uppercase(str):
    new_str = ""
    for c in str:
        new_str += "%c" % _upper(c)
    print("{:s}".format(new_str))
