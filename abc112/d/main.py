#!/usr/bin/env python3

N, M = map(int,(input().split()))

# furui = [1] * M

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

primes = set(make_divisors(M))

ans = 0

for prime in primes:
    if prime * N <= M:
        ans = max(ans, prime)

print(ans)