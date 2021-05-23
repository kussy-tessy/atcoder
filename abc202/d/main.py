#!/usr/bin/env python3

A, B, K = map(int,(input().split()))

from math import factorial

def first(a_cnt, b_cnt, K):
    if a_cnt == 0:
        return (a_cnt+b_cnt, 'b')
    if b_cnt == 0:
        return (0, 'a')
    split = factorial(a_cnt+b_cnt-1) // (factorial(a_cnt-1) * factorial(b_cnt))
    if K <= split:
        return (split, 'a')
    else:
        return (split, 'b')

res = ''
a_cnt = A
b_cnt = B
for i in range(A+B):
    split, char = first(a_cnt, b_cnt, K)
    res += char
    if char == 'a':
        a_cnt -= 1
    if char == 'b':
        b_cnt -= 1
        K -= split

print(res)
    