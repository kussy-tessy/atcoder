#!/usr/bin/env python3

import bisect

N = input()
As = list(map(int,(input().split())))
Bs = list(map(int,(input().split())))
Cs = list(map(int,(input().split())))


# 計算が間に合わない
As.sort()
Bs.sort()
Cs.sort()

"""
ans = 0
b = 0
c = 0
for i in range(len(As)):
    for j in range(b, len(Bs)):
        if Bs[j] > As[i]:
            b = j
            # print('b', b)
            for k in range(c, len(Cs)):
                if Cs[k] > Bs[j]:
                    c = k
                    # print('c', c)
                    ans += len(Cs) - k
                    break
            b = 0
    c = 0

print(ans)
"""

# Bを固定する
# Ai < Bjとなる個数 × Bj < Ckとなる個数を足せばよい
# iとkの具体的な値は二分探索でよい
# 二分探索はbisectがとてもかんたん

ans = 0

for B in Bs:
    l = bisect.bisect_left(As, B)
    r = len(Cs) - bisect.bisect_right(Cs, B)
    ans += l * r

print(ans)