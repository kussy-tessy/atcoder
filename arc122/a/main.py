#!/usr/bin/env python3

N = int(input())
As = list(map(int,(input().split())))

MOD = 10**9 + 7

if N == 1:
    print(As[0])
    exit()

dp1 = [[0] * (N-1) for _ in range(2)]
dp2 = [[0] * (N-1) for _ in range(2)]

"""
dp1[j][i]: i番目の符号を入れるところでj=0のとき+で終わるパターンの数、j=1のとき-で終わるパターンの数
dp2[j][i]: 上のルールで総和
"""

dp1[0][0] = 1
dp1[1][0] = 1
dp2[0][0] = As[0] + As[1]
dp2[1][0] = As[0] - As[1]

for i in range(N-2):
    dp1[0][i+1] = dp1[0][i] + dp1[1][i]
    dp1[1][i+1] = dp1[0][i]
    dp1[0][i+1] %= MOD
    dp1[1][i+1] %= MOD
    dp2[0][i+1] = (dp2[0][i] + dp2[1][i]) + As[i+2] * dp1[0][i+1]
    dp2[1][i+1] = dp2[0][i] - As[i+2] * dp1[1][i+1]
    dp2[0][i+1] %= MOD
    dp2[1][i+1] %= MOD

print((dp2[0][N-2] + dp2[1][N-2]) % MOD)

"""
sums = As[0] * pow(2, N-1, MOD)

sub = 0

print(f'{sums=}')
s = N - 3
if N % 2 == 0:
    for i in range(1, N // 2 - 1):
        sub = (As[i] + As[-i]) * s * 2
        s += 2
    sub += s
else:
    for i in range(1, N // 2):
        sub = (As[i] + As[-i]) * s * 2
        s += 2

print(f'{sub=}')

print((sums - sub) % MOD)
"""