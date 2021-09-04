#!/usr/bin/env python3
import bisect

N, Q = map(int,(input().split()))
As = list(map(int,(input().split())))
Ks = []

for _ in range(Q):
    Ks.append(int(input()))

# up_c = {}

# up_c[As[0]] = 1
up_c = [[As[0], 1]]

for i in range(1, len(As)):
    dif = As[i] - As[i-1]
    last = up_c[-1]
    if dif >= 2:
        up_c.append([last[0]+dif-1, last[1]+1])
    elif dif == 1:
        up_c[-1] = [last[0], last[1]+1]

# print(f"{up_c=}")
c = [up[0] for up in up_c]
# print(f"{c=}")

for K in Ks:
    idx = bisect.bisect(c, K)
    # print(idx)
    if idx > 0:
        cnt = up_c[idx-1]
        print(K+cnt[1])
    else:
        print(K)
# print(up_c)

# """
# 4 1
# 3 4 5 8
# 2
# """