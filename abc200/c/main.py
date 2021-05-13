#!/usr/bin/env python3
import collections
from scipy.special import comb

N = int(input())
As = list(map(int,(input().split())))

As_mod = [A % 200 for A in As]

As_mod_counter = collections.Counter(As_mod)

ans = 0
for c_cnt in As_mod_counter.values():
    ans += comb(c_cnt, 2, exact=True)

print(ans)