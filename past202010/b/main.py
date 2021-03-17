#!/usr/bin/env python3
from math import floor
from sys import exit

# print('input >>')
X, Y = map(int,(input().split()))
if Y == 0:
    print('ERROR')
    exit()

quo = X / Y
quo *= 100
quo = floor(quo)
quo /= 100

# print('-----output-----')
print(f'{quo:.2f}')