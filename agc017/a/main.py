#!/usr/bin/env python3

from collections import Counter
from scipy.special import comb

def comb_odd(n):
    res = 0
    for i in range(0, n+1, 2):
        res += comb(n, i, exact=True)
    return res

def comb_even(n):
    res = 0
    for i in range(1, n, 2):
        res += comb(n, i, exact=True)
    return res

N, P = map(int,(input().split()))
As = list(map(int,(input().split())))

As_oe = [0] * N
for i, A in enumerate(As):
    if A % 2 == 0: # 偶数なら0
        As_oe[i] = 0
    else: # 奇数なら1
        As_oe[i] = 1

counters = Counter(As_oe)
even = counters[0] # 偶数の数
odd = counters[1] # 奇数の数

if P % 2 == 0: # 偶数のとき
    print(2**even * comb_odd(odd))
else: # 奇数のとき
    print(2**even * comb_even(odd))

"""
あ、bit全探索では間に合わないっすね
# 1は残す、0は食べる
products = product([0, 1], repeat=N)

patterns = 0
for p in products:
    biscuits = 0
    for i, p_ in enumerate(p):
        if p_ == 1:
            biscuits += As[i]
    if biscuits % 2 == P:
        patterns = 0

print('No')
"""