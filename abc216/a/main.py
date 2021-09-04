#!/usr/bin/env python3

xy = input()

[xs, ys] = xy.split('.')

x = int(xs)
y = int(ys)

if 0 <= y <= 2:
    print(str(x)+'-')
elif 3 <= y <= 6:
    print(x)
else:
    print(str(x)+'+')