#!/usr/bin/env python3

N, K = map(int,(input().split()))
ABs = []
for _ in range(N):
    ABs.append(tuple(map(int,(input().split()))))

ABs.sort(key=lambda AB:AB[0])

for AB in ABs:
    K -= AB[1]
    if K <= 0:
        print(AB[0])
        exit()