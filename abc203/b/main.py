#!/usr/bin/env python3

N, K = map(int,(input().split()))

ans = 0

for n in range(1, N + 1):
    for k in range(1, K + 1):
        ans += n * 100 + k

# print(sum([N * 100 + k for k in range(1, K+1)]))
print(ans)