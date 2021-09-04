#!/usr/bin/env python3

N = int(input())
As = list(map(int,(input().split())))

As_abs = [abs(A) for A in As]
As_abs.sort()
minus_cnt = sum([True for A in As if A < 0])
if minus_cnt % 2 == 1:
    print(sum(As_abs[1:]) - As_abs[0])
else:
    print(sum(As_abs))

