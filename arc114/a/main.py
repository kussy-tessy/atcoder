#!/usr/bin/env python3
from math import gcd
from functools import reduce
from itertools import product

# https://note.nkmk.me/python-prime-factorization/
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

# https://note.nkmk.me/python-gcd-lcm/
def my_lcm_base(x, y):
    return (x * y) // gcd(x, y)

def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)

N = int(input())
Xs = list(map(int,(input().split())))

primes = set()
for X in Xs:
    X_primes = set(prime_factorize(X))
    for X_prime in X_primes:
        primes.add(X_prime)

primes_ls = list(primes)
primes_ls.sort()
cands = product([0, 1], repeat=len(primes_ls))
ans = 10 ** 1000
for cand in cands:
    x = 1
    for prime_, cand_ in zip(primes_ls, cand):
        x *= prime_ if cand_ == 1 else 1
    # print(f'{x=}について調べます')
    is_ok = True
    for X in Xs:
        if gcd(X, x) == 1:
            # print(f'{X=},{x=}なのでだめ')
            is_ok = False
            break
    if is_ok:
        ans = min(ans, x)

print(ans)