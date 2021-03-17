#!/usr/bin/env python3
import itertools

def calc_score(target, a, b, c, d):
    if target[b-1] - target[a-1] == c:
        return d
    else:
        return 0

N, M, Q = map(int,(input().split()))
abcds = []
for _ in range(Q):
    abcds.append(tuple(map(int,(input().split()))))

combination = itertools.combinations_with_replacement([i for i in range(1, M+1)], N)
res = 0

for c in combination:
    score = 0
    for abcd in abcds:
        score += calc_score(c, *abcd)
    res = max(res, score)

print(res)