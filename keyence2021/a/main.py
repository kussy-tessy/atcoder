#!/usr/bin/env python3

N = int(input())
As = list(map(int,(input().split())))
Bs = list(map(int,(input().split())))

now_max = 0
As_max = 0

for i in range(len(As)):
    As_max = max(As_max, As[i])
    now_max = max(now_max, Bs[i] * As_max)
    print(now_max)