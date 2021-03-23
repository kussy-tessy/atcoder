import itertools
import numpy as np
import math

# print('input >>')
N = int(input())
towns = []
for _ in range(N):
    x, y = map(int,(input().split()))
    towns.append(np.array([x,y]))

sum = 0
perms = itertools.permutations(range(N), N)

distances = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        distances[i][j] = np.linalg.norm(towns[i]-towns[j])

sum = 0
for p in perms:
    distance = 0
    for i in range(N-1):
        distance += distances[p[i]][p[i + 1]]
    sum += distance

# print('----------output----------')
print(sum / math.factorial(N))