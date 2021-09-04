#!/usr/bin/env python3
from collections import deque

N, K = map(int,(input().split()))
ABs = {}
# ABs[0] = K 
for _ in range(N):
    # ABs.append(tuple(map(int,(input().split()))))
    A, B = map(int,(input().split()))
    if not A in ABs:
        ABs[A] = 0
    ABs[A] += B

ABs_sorted = sorted(ABs.items(), key=lambda x:x[0])

pre_A = 0
pre_K = K
for A, B in ABs_sorted:
    K -= A - pre_A
    if K < 0:
        # print(f"{pre_A=}, {pre_K=}")
        # print(f"{pre_A+pre_K=}")
        print(pre_A+pre_K)
        exit()
    K += B
    # print(f"{K=}")
    # K -= A
    # K += B 
    pre_A = A
    pre_K = K
print(pre_A + K)

"""
4 1
1 100
2 100
3 100
1000 20
"""


# for A, B in ABs:
#     K += B
#     if A > K:
#         print(A)

# print(A)

# ABs_sorted = sorted(ABs.items(), key=lambda x:x[0])
# q = deque(ABs_sorted)
# print(q)

# p = 0

# # A村でB円手に入る
# while K >= 0:
#     print(f"{p=}")
#     if not (p in ABs) or ABs[p] == 0:
#         next_A, next_B = q.popleft()
#         ABs[next_A] = 0
#         next_p = min(p+K, next_A)
#         print(f"{next_p=}")
#         K -= next_p - p
#         p = next_p
#         print(f"{p=}")
#     else:
#         K += ABs[next_B]
#         print(f"{next_B=}")
#     if len(q) == 0:
#         break

# print(f"{K=}")
# print(p + K)

# """
# 4 1
# 1 100
# 2 100
# 3 100
# 10 100
# """