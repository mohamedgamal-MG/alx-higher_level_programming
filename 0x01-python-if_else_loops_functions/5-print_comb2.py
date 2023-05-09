#!/usr/bin/python3
for a in range(00, 100):
    print("{:02d}".format(a), end='\n' if a == 99 else ", ")
