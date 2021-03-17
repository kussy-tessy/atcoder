import numpy as np

# print('input >>')
H, W, M = map(int,(input().split()))
bombs = []
for _ in range(M):
    bombs.append(tuple(map(int,(input().split()))))

grid = [[0] * W for _ in range(H)]

for bomb in bombs:
    h = bomb[0] - 1
    w = bomb[1] - 1
    grid[h][w] = 1

grid = np.array(grid)

hsum = np.sum(grid, axis=0)
wsum = np.sum(grid, axis=1)

hmaxi = np.argmax(hsum)
hmax = np.argmax(hsum)

# print(hsum)
# print(wsum)

# print('-----output-----')
print(max(hsum) + max(wsum) - 1)