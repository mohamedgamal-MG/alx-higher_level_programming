#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lastdigit = number % 10
else:
    lastdigit = ((number * -1) % 10) * -1
massage = "Last digit of {} is {} and is".format(number, lastdigit)
if lastdigit > 5:
    print(f"{massage} greater than 5")
elif lastdigit == 0:
    print(f"{massage} 0")
elif lastdigit < 6:
    print(f"{massage} less than 6 and not 0")
