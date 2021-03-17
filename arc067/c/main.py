#!/usr/bin/env python3
import collections

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

def count_yaku(dic):
    ls = [v+1 for k, v in dic.items()]
    res = 1
    for l in ls:
        res *= l
    return res

N = int(input())
MOD = 10 ** 9 + 7

yakus_conv = {}
for i in range(1, N+1):
    yakus = prime_factorize(i)
    yakus_dict = collections.Counter(yakus)
    for yaku, cnt in yakus_dict.items():
        if not yaku in yakus_conv:
            yakus_conv[yaku] = 0
        yakus_conv[yaku] += cnt

print(count_yaku(yakus_conv) % MOD)