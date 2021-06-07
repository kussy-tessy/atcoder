#!/usr/bin/env python3

N = int(input())
As = list(map(int,(input().split())))

"""
ans = float('inf')
for i in range(1, len(As)):
    As_f = As[:i]
    As_s = As[i:]

    p = 0
    for a in As_f:
        p |= a
    q = 0
    for b in As_s:
        q |= b
    ans = min(ans, p ^ q)

print(ans)
"""

ans = float('inf')
for i in range(2 ** (N-1)):
    or_ = 0
    xor = 0
    # print(bin(i))
    for j in range(N):
        # フラグが立っていない
        if (i >> j) & 1 == 0:
            or_ |= As[j]
            # print('a', j, or_)
        # フラグが立っている
        if (i >> j) & 1 == 1:
            or_ |= As[j]
            # print('b', j, or_)
            xor ^= or_
            or_ = 0 # リセット
    xor ^= or_ # 最後
    # print(xor)
    ans = min(ans, xor)

print(ans)