#!/usr/bin/env python3
from sys import exit
from decimal import *

N, X = map(int,(input().split()))
VPs = []

for _ in range(N):
    VPs.append(tuple(map(int,(input().split()))))

now_al = 0
for i, VP in enumerate(VPs):
    now_al += Decimal(str(VP[0])) * Decimal(str(VP[1])) / Decimal('100')
    if now_al > Decimal(str(X)):
        print(i+1)
        exit()

print(-1)