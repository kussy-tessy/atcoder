from itertools import product
import numpy as np
import sys

# print('input >>')
N, M, X = map(int,(input().split()))

Cs = []

for _ in range(N):
    Cs.append(list(map(int,(input().split()))))

Cs = np.array(Cs)

patterns = product([0, 1], repeat=N)

ans = 10**12

for pattern in patterns:
    # print(pattern)
    for i in range(len(pattern)):
        en = 0
        unds = np.array([0]*M)
        for p in range(len(pattern)):
            if pattern[p] == 1:
                unds += Cs[p, 1:]
                en += Cs[p][0]
                if all([u >= X for u in unds]):
                    # print('p', pattern)
                    ans = min(ans, en)

if ans == 10**12:
    print(-1)
    sys.exit()

# print('-----output-----')
print(ans)