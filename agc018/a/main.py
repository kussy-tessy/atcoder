#!/usr/bin/env python3
import math
from functools import reduce

def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

N, K = map(int,(input().split()))
As = list(map(int,(input().split())))

As_gcd = my_gcd(*As)
As_max = max(As)

ok = As_max >= K and (As_max - K) % As_gcd == 0

print('POSSIBLE' if ok else 'IMPOSSIBLE')