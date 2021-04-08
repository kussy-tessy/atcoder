#!/usr/bin/env python3
from scipy.special import comb

n = int(input())
As = list(map(int,(input().split())))

# for A in As:
#     for B in As:
#         print(f'{A=}, {B=}', comb(A, B))

A_max = max(As)
A_max_half = A_max / 2

A_max_half_diff = [(A, abs(A-A_max_half)) for A in set(As)-set([A_max])]
A_max_half_diff.sort(key=lambda x:x[1])

# よく分からんので最初の3つくらい候補にしとこ。たぶん最初だろうけど
# cands = A_max_half_diff[:3]

# print(cands)
# ans = 0
# rc = 0
# for cand in cands:
#     c = comb(A_max, cand[0])
#     if c > ans:
#         rc = cand[0]

print(A_max, A_max_half_diff[0][0])
