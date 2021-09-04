#!/usr/bin/env python3

N  = int(input())
ps = list(map(int,(input().split())))

ans = [None] * N

for i, p in enumerate(ps):
    ans[p-1] = str(i+1)


print(' '.join(ans))