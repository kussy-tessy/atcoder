#!/usr/bin/env python3

N, D, H = map(int,(input().split()))
dhs = []
for _ in range(N):
    dhs.append(tuple(map(int,(input().split()))))

def calc(d, h):
    return max(0, h - d * (H-h) / (D-d))

ans = 0

for dh in dhs:
    d, h = dh
    ans = max(ans, calc(d,h))

print(ans)