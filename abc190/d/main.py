#!/usr/bin/env python3

import math

N = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

ans = 0
# for n in range(1, N):
#     if (2*N) % n == 0 and (2*N//n - n + 1) % 2 == 0:
#         ans += 1

divisors = make_divisors(2*N)

for n in divisors:
    if (2*N//n - n + 1) % 2 == 0:
        ans += 1

print(ans)
