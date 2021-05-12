#!/usr/bin/env python3
import numpy as np
import itertools as it

# 記念提出！

N = int(input())

ABCDEs = []

for _ in range(N):
    ABCDEs.append(list(map(int,(input().split()))))

print(ABCDEs)

ABCDEs = np.array(ABCDEs)
# print(ABCDEs[0, :])

As_max = np.argsort(ABCDEs[:, 0])[:3:-1]
Bs_max = np.argsort(ABCDEs[:, 1])[:3:-1]
Cs_max = np.argsort(ABCDEs[:, 2])[:3:-1]
Ds_max = np.argsort(ABCDEs[:, 3])[:3:-1]
Es_max = np.argsort(ABCDEs[:, 4])[:3:-1]

print(np.argsort(ABCDEs[:, 0])[:2:-1])
cand = set([*As_max, *Bs_max, *Cs_max, *Ds_max, *Es_max])
# print(cand)
combs = it.combinations(cand, 3)

ans = 0
for comb in combs:
    c1, c2, c3 = comb
    mmax = ABCDEs[c1].copy()
    mmax = np.vstack([mmax, ABCDEs[c2]])
    mmax = np.vstack([mmax, ABCDEs[c3]])
    mmin = min(max(mmax[:, 0]),max(mmax[:, 1]),max(mmax[:, 2]),
        max(mmax[:, 3]),max(mmax[:, 4]))
    ans = max(ans, mmin)

print(ans)