#!/usr/bin/env python3

# print('input >>')

N, M = map(int,(input().split()))
grid = []

# 外側を囲む
grid.append('.' * (M+2))
for _ in range(N):
    grid.append('.' + input() + '.')
grid.append('.' * (M+2))

# print('\n'.join(grid))

# print('-----output-----')

for i in range(1, N+1):
    for j in range(1, M+1):
        sharp = 0
        for (x, y) in ((i-1, j-1), (i, j-1), (i+1, j-1), (i-1, j), (i, j), (i+1, j), (i-1, j+1), (i, j+1), (i+1, j+1)):
            # print(x, y)
            if grid[x][y] == '#':
                sharp += 1
        print(sharp, end='')
    print()