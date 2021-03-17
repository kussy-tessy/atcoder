#!/usr/bin/env python3

def f(x):
    x_list = list(str(x))
    g1 = ''.join(sorted(x_list, reverse=True))
    g2 = ''.join(sorted(x_list, reverse=False))
    return int(g1)-int(g2)

N, K = map(int,(input().split()))

for i in range(K):
    N = f(N)

print(N)