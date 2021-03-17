#!/usr/bin/env python3

N = int(input())
As = list(map(int,(input().split())))

As.sort()

res = 0
sum_ = sum(As)

for i in range(len(As)):
    sum_ -= As[i]
    res += sum_ - As[i] * (len(As)-(i+1))
    # print(sum_ ,res)

print(res)

