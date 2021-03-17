#!/usr/bin/env python3

N = int(input())
APXs = []
for _ in range(N):
    APXs.append(tuple(map(int,(input().split()))))

ans = float('inf')

for A, P, X in APXs:
    if A < X:
        ans = min(P, ans)

print(-1 if ans == float('inf') else ans)