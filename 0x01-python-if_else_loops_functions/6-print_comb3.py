#!/usr/bin/python3
for x in range(0, 100):
    a = x % 10
    b = x / 10
    if b < a and x != 89:
        print("{:02}, ".format(x), end="")
    elif x == 89:
        print("{}".format(x))
