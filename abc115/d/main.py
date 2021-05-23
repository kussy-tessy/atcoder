#!/usr/bin/env python3
from math import ceil

N, X = map(int,(input().split()))
layers = [0] * (N+1)
patis = [0] * (N+1)

layers[0] = 1
patis[0] = 1

for i in range(1, N+1):
    layers[i] = 3 + layers[i-1] * 2
    patis[i] = 1 + patis[i-1] * 2

# レベルNバーガーの下層X枚に含まれるパティの数
def pati(N, X):
    if N == 0:
        return 1
    if X == 1:
        return 0
    if X < ceil(layers[N] / 2):
        return pati(N-1, X-1)
    if X == ceil(layers[N] / 2):
        return patis[N-1] + 1
    if X < layers[N]:
        return patis[N-1] + 1 + pati(N-1, X - ceil(layers[N] / 2))
    if X == layers[N]:
        return patis[N]

print(pati(N, X))
