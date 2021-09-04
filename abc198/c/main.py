#!/usr/bin/env python3
from math import ceil, sqrt

R, X, Y = map(int,(input().split()))
d = sqrt((X**2 + Y **2))

if d > R:
    print(ceil(d / R))
elif d == R:
    print(1)
else:
    print(2)