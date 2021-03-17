#!/usr/bin/env python3
from math import gcd

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

A, B = map(int,(input().split()))

gcd_ = gcd(A, B)
fracs = make_divisors(gcd_)

for i, frac in enumerate(fracs):
    if frac > 0:
        for j in range(i+1, len(fracs)):
            if gcd(fracs[j], frac) > 1:
                fracs[j] = 0
                # print(fracs)
        
ans = sum([1 if frac > 0 else 0 for frac in fracs])

print(ans)