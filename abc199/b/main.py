#!/usr/bin/env python3

N = int(input())
As = list(map(int,(input().split())))
Bs = list(map(int,(input().split())))

ans = set(range(1, 1001))

for A, B in zip(As, Bs):
    the_range = set(range(A, B+1))
    ans = ans.intersection(the_range)

print(len(ans))