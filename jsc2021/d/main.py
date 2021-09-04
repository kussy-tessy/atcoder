#!/usr/bin/env python3

N, P = map(int,(input().split()))

MOD = 10**9 + 7

# ans = P-1

# for i in range(N-1):
#     ans *= P-2
#     ans %= MOD

# ans = ((P-1)*((P-2)**(N-1))) % MOD
ans = (P-1) * pow(P-2, N-1, MOD)

print(ans % MOD)
