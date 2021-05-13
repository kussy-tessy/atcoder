#!/usr/bin/env python3

H, W = map(int,(input().split()))
grid = []

for _ in range(H):
    grid.append(list(map(int,(input().split()))))

ans = []

for h in range(len(grid)):
    for w in range(len(grid[h])):
        if grid[h][w] % 2 == 1:
            if w != len(grid[h])-1:
                grid[h][w+1] += 1
                ans.append([h+1, w+1, h+1, w+1+1])
            elif w == len(grid[h])-1 and h != len(grid)-1:
                grid[h+1][w] += 1
                ans.append([h+1, w+1, h+1+1, w+1])

print(len(ans))
for ans_l in ans:
    print(' '.join([str(t) for t in ans_l]))
