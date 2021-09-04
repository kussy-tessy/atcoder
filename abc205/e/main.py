#!/usr/bin/env python3
from scipy.special import comb

N, M, K = map(int,(input().split()))
MOD = 10**9 + 7
ans = 0

"""
for n in range(1, K+1):
    ans += comb(K+n, n, exact=True) * comb(N+1-(K+n), M-n, exact=True)
    ans %= MOD

print(ans)
"""

