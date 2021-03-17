#!/usr/bin/env python3

H, W = map(int,(input().split()))

A_grid = []

for _ in range(H):
    A_grid.append(list(map(int,(input().split()))))

min_ = 100000000

for line in A_grid:
    for cell in line:
        min_ = min(cell, min_)

res = 0

for line in A_grid:
    for cell in line:
        res += cell - min_

print(res)