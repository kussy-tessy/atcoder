#!/usr/bin/env python3

N, M = map(int,(input().split()))
grid = []

# 周りを囲む
# grid.append('.' * (M+2))
for _ in range(N):
    grid.append(input())
# grid.append('.' * (M+2))

cand = set()

for i in range(N):
    for j in range(M):
        """
        derarenai = True
        for (x, y) in ((i, j-1), (i-1, j), (i+1, j), (i, j+1)):
            if 0 <= x < M and 0 <= y < N:
                if grid[x][y] == '.':
                    derarenai = False
        if derarenai:
            for (x, y) in ((i, j-1), (i-1, j), (i+1, j), (i, j+1)):
                if 0 <= x < M and 0 <= y < N:
                    if grid[x][y] == '#':
                        cand.add((x, y))
        """
        if grid[i][j] == '#':
            derarenai = True
            for (x, y) in ((i-1, j-1), (i+1, j-1), (i-1, j+1), (i+1, j+1)):
                if 0 <= x < M and 0 <= y < N:
                    
                    

print(len(cand))