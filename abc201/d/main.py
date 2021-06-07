#!/usr/bin/env python3

H, W = map(int,(input().split()))
grid = []

for _ in range(H):
    grid.append(list(input()))

taka = 0
aoki = 0
now = [0, 0]

for i in range((H-1)+(W-1)):
    # +の方を優先
    