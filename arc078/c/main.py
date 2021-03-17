#!/usr/bin/env python3

N = int(input())
As = list(map(int,(input().split())))

snuke = 0
arai = sum(As)
ans = 10 ** 20

for i in range(N-1):
    snuke += As[i]
    arai -= As[i]
    ans = min(ans, abs(snuke-arai))

print(ans)