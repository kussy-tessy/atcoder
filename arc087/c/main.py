#!/usr/bin/env python3

from collections import Counter

N = input()
As = list(map(int,(input().split())))

c = Counter(As)

res = 0

# print(c)
for num, cnt in c.items():
    if num <= cnt:
        res += cnt - num
    else:
        res += cnt

print(res)