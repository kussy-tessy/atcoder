#!/usr/bin/env python3
# import numpy as np

N, M = map(int,(input().split()))

N_image = []
M_image = []

# def is_same(X, Y):
#     for r_i, r_j in zip(X, Y):
#         for i, j in zip(r_i, r_j):
#             print(i, j)
#             if not i == j:
#                 return False
#     return True
 
for _ in range(N):
    N_image.append(list(input()))

for _ in range(M):
    M_image.append(list(input()))

# N_image = np.array(N_image)
# M_image = np.array(M_image)

for i in range(N-M+1):
    for j in range(N-M+1):
        is_ok = True
        for k in range(M):
            for l in range(M):
                # print(N_image[i+k][j+l], M_image[k][l], k, l)
                if not N_image[i+k][j+l] == M_image[k][l]:
                    is_ok = False
        if is_ok:
            print('Yes')
            exit()

print('No')