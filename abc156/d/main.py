#!/usr/bin/env python3

n, a, b = map(int,(input().split()))


MOD = 10**9 + 7
# MOD = 13

def c(n, r):
    if r > n / 2:
        r = n - r
    
    x = n
    b = 1
    for _ in range(r):
        b *= x
        b %= MOD
        x -= 1

    y = r
    for _ in range(r):
        b *= pow(y, -1, MOD)
        b %= MOD
        y -= 1

    return b % MOD

print(((pow(2, n, MOD) -1) -c(n, a) -c(n, b)) % MOD)
