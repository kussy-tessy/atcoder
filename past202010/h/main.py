#!/usr/bin/env python3

from sys import exit
import numpy as np

# print('input >>')
N, M, K = map(int,(input().split()))
grid = []

for _ in range(N):
    grid.append(input())

imos = {}

for n in '0123456789':
    imos_grid = np.array([[0] * (M+1) for _ in range(N+1)])
    # print(imos_grid)
    for i in range(N):
        for j in range(M):
            plus = 1 if grid[i][j] == n else 0
            imos_grid[i][j] = imos_grid[i][j-1] + imos_grid[i-1][j] -imos_grid[i-1][j-1] + plus
    # imos_grid = imos_grid[:-1, :-1]
    imos[n] = imos_grid

    # print(imos_grid)

for p in range(min(N, M), 0, -1):
    for i in range(N - p + 1):
        for j in range(M - p + 1):
            for n, imos_grid in imos.items():
                # print(f'i={i}, j={j}, p={p}') 
                # print(f'{imos_grid[i+p][j+p]} - {imos_grid[i][j]}')
                # print(f'{n}, {p**2}, {imos_grid[i+p-1][j+p-1]} - {imos_grid[i][j]}')
                if p**2 - (imos_grid[i+p-1][j+p-1] - imos_grid[i-1][j-1]) <= K:
                    # print(f'{n}, {p}, {i}, {j}, {imos_grid[i+p-1][j+p-1]} - {imos_grid[i][j]}')
                    print(p)
                    exit()

# print('-----output-----')

# 3 4 2
# 1123
# 1214
# 1810
