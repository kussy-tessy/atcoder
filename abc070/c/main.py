#!/usr/bin/env python3

from math import gcd
from functools import reduce

def dcg_multi(*nums):
    return reduce(gcd, nums)
def lcm(x, y):
    return (x * y) // gcd(x, y)
def lcm_multi(*nums):
    return reduce(lcm, nums, 1)

N = int(input())
Ts = []
for _ in range(N):
    Ts.append(int(input()))

print(lcm_multi(*Ts))
