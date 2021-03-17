#!/usr/bin/env python3

N = int(input())
vec_a = list(map(int,(input().split())))
vec_b = list(map(int,(input().split())))

naiseki = 0

for i in range(N):
    naiseki += vec_a[i] * vec_b[i]

if naiseki == 0:
    print('Yes')
else:
    print('No')