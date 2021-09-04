#!/usr/bin/env python3
from math import floor

N = int(input())

price = floor(N * 1.08)

if price < 206:
    print('Yay!')
elif price > 206:
    print(':(')
else:
    print('so-so')