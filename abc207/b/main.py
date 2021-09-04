#!/usr/bin/env python3
from math import ceil

A, B, C, D = map(int,(input().split()))

if C*D- B != 0:
    sol = A / (C*D-B)
else:
    sol = -1

if sol <= -1:
    print(-1)
else:
    print(ceil(sol))