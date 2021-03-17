#!/usr/bin/env python3
from itertools import product

H, W, K = map(int,(input().split()))
HWs = []

for _ in range(H):
    HWs.append(list(input()))
# sel_Hとsel_Wはboolean list
def cnt(sel_H: list, sel_W: list):
    black = 0
    for i in range(H):
        for j in range(W):
            if HWs[i][j] == '#' and sel_H[i] == False and sel_W[j] == False:
                black += 1
    return black

products_H = list(product([True, False], repeat=H))
products_W = list(product([True, False], repeat=W))

# print([product_H for product_H in products_H])
ans = 0
for product_H in products_H:
    for product_W in products_W:
        if cnt(product_H, product_W) == K:
            ans += 1
            # print(product_H, product_W)

print(ans)