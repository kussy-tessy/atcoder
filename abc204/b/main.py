#!/usr/bin/env python3

N = int(input())
As = list(map(int,(input().split())))

ans = 0

for A in As:
    ans += max(0, A-10)

print(ans)