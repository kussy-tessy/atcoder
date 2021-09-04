#!/usr/bin/env python3

N, A, X, Y = map(int,(input().split()))

if N > A:
    ans = A * X + (N-A) * Y
else:
    ans = N * X

print(ans)