#!/usr/bin/env python3

N = int(input())
As = list(map(int,(input().split())))

MOD = 10**9 + 7

# p = 1
# for A in As:
#     p *= A + 1
#     p %= MOD

# print(p)

As.append(0)
As = sorted(list(set(As)))

ans = 1
for i in range(1, len(As)):
    ans *= (As[i] - As[i-1] + 1)
    ans %= MOD

print(ans)