#!/usr/bin/env python3

from collections import Counter
from scipy.special import comb

N = int(input())
As = list(map(int,(input().split())))

As_counter = Counter(As)

all_p = comb(N, 2, exact=True)

dif = 0
for (c, cnt) in As_counter.items():
    if cnt > 1:
        dif += comb(cnt, 2, exact=True)

print(all_p - dif)