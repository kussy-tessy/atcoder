#!/usr/bin/env python3
from sys import exit

K = int(input())

# 余りについて考えると鳩の巣原理より高々Kまで調べれば十分
prev = 0
for i in range(K):
    now = (prev * 10 + (7 % K)) % K
    # print(now)
    if now == 0:
        print(i+1)
        exit()
    prev = now

print(-1)

# まあまずは愚直解
"""
for i in range(1, 100000):
    x = int('7' * i)
    if x % K == 0:
        print(i)
        exit()

input(-1)
"""

"""
# だめだサンプルケースですら遅すぎて通らねえ
for i in range(1000000):
    x = K * i
    if all([c == '7' for c in str(x)]):
        print(len(str(x)))
        exit()

print(-1)
"""

"""
x = 0
for i in range(1000000):
    # print(x)
    x = x * 10 + 7
    if x % K == 0:
        print(i+1)
        exit()

input(-1)
"""