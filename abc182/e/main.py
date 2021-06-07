#!/usr/bin/env python3

import random

H, W, N, M = map(int,(input().split()))
# ABs = []
# CDs = []
# for _ in range(N):
#     ABs.append(tuple(map(int,(input().split()))))
# for _ in range(M):
#     CDs.append(tuple(map(int,(input().split()))))

# https://zenn.dev/wapa5pow/articles/abc182-e-466c22605203cd42efd4
grid = [[0] * (W+2) for i in range(H+2)]


# 0 未決定
# 2 ライト
# 1 照らされている
# -1 ブロック

# 境界の処理が煩雑。。。
for _ in range(N):
    i, j = map(int, (input().split()))
    grid[i][j] = 2
for _ in range(M):
    i, j = map(int, (input().split()))
    grid[i][j] = -1

H = H + 2
W = W + 2

# 探索方向→
for i in range(H):
    enlighten = False
    for j in range(W):
        if grid[i][j] == 2:
            enlighten = True
        if grid[i][j] == -1:
            enlighten = False
        if enlighten and grid[i][j] == 0:
            grid[i][j] = 1

# 探索方向←
for i in range(H):
    enlighten = False
    for j in range(W)[::-1]:
        if grid[i][j] == 2:
            enlighten = True
        if grid[i][j] == -1:
            enlighten = False
        if enlighten and grid[i][j] == 0:
            grid[i][j] = 1

# 探索方向↓
for j in range(W):
    enlighten = False
    for i in range(H):
        if grid[i][j] == 2:
            enlighten = True
        if grid[i][j] == -1:
            enlighten = False
        if enlighten and grid[i][j] == 0:
            grid[i][j] = 1

# 探索方向↑
for j in range(W):
    enlighten = False
    for i in range(H)[::-1]:
        if grid[i][j] == 2:
            enlighten = True
        if grid[i][j] == -1:
            enlighten = False
        if enlighten and grid[i][j] == 0:
            grid[i][j] = 1

# for g in grid:
#     print(g)

ans = 0
for i in range(1, H-1):
    for j in range(1, W-1):
        if grid[i][j] > 0:
            ans += 1

print(ans)