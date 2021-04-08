#!/usr/bin/env python3
from collections import Counter

N = int(input())
As = list(map(int,(input().split())))

As_counter = Counter(As)

cands = [A for A in As if As_counter[A] >= 2]
cands_l = list(set(cands))
cands_l.sort(reverse=True)

# print(cands_l)
# 長方形を作れない
# 一番長いのが4本以上ある
if len(cands_l) >= 1 and As_counter[cands_l[0]] >= 4:
    print(cands_l[0] ** 2)
elif len(cands_l) <= 0:
    print(0)
else:
    print(cands_l[0] * cands_l[1])
