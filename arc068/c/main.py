#!/usr/bin/env python3
from math import ceil

x = int(input())

if x <= 6:
    print(1)
elif x <= 11:
    print(2)
else:
    t = x // 11
    mod = x % 11
    if mod == 0:
        # print('x')
        print(t * 2)
    elif mod <= 6:
        # print('y')
        print(t * 2 + 1)
    else:
        # print('z')
        print(t * 2 + 2)