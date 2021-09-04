#!/usr/bin/env python3

H, W, K = map(int,(input().split()))

grid = []

for _ in range(H):
    grid.append(list(input()))

ans = []

no = 0
# print(grid)

# 番号つける
for i in range(H):
    for j in range(W):
        if grid[i][j] == '.':
            grid[i][j] = 0
        if grid[i][j] == '#':
            no += 1
            grid[i][j] = no

# 右方向
for i in range(H):
    no = 0
    for j in range(W):
        if grid[i][j] != 0:
            no = grid[i][j]
        grid[i][j] = no

# 左方向
for i in range(H):
    no = 0
    for j in range(W-1, -1, -1):
        if grid[i][j] != 0:
            no = grid[i][j]
        grid[i][j] = no

# for row in grid:
#     for cell in row:
#         print(cell, end=' ')
#     print()

# 下方向
for j in range(W):
    no = 0
    for i in range(H):
        if grid[i][j] != 0:
            no = grid[i][j]
        grid[i][j] = no

# 上方向
for j in range(W):
    no = 0
    for i in range(H-1, -1, -1):
        if grid[i][j] != 0:
            no = grid[i][j]
        grid[i][j] = no

for row in grid:
    print(' '.join(list(map(str, row))))

# for row in grid:
#     strs = 0
#     for cell in row:
#         if cell == '#':
#             strs += 1
#     if strs == 0:
#         ans.append([no] * 1) # 上と同じ
#     elif strs == 1:
#         no += 1
#         ans.append([no] * 1) # 全部そのケーキ
#     elif strs >= 2:
#         nl = []
#         no += 1
#         for cell in row:
#             if cell == '.': # いちごでない
#                 nl.append(no)
#             else: # いちご
#                 no += 1
#                 nl.append(no)
#         ans.append(nl)

for al in ans:
    for c in al:
        print(c, end=' ')
    print()