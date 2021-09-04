#!/usr/bin/env python3

N = int(input())
Ts = list(map(int,(input().split())))
gokei = sum(Ts)

"""
dp = [[0] * (gokei+5) for _ in range(N+5)]

for i in range(N+5):
    for j in range(gokei+5):
        if j >= Ts[i]:
            dp[i][j+1] = max(dp[i][j-Ts[i]], dp[i][j])
        else:
            dp[i][j+1] = dp[i][j]

for row in dp:
    print(row)
"""

# https://qiita.com/u2dayo/items/1ed77ef0ac2cf3de7c15
"""
dp[i][j]: i番目までの料理を使って、j分の料理を作れるか
"""

dp = [[False] * (gokei + 1) for _ in range(N+1)]

dp[0][0] = True

for i in range(N):
    t = Ts[i] # i番目の料理のかかる時間
    for j in range(gokei + 1):
        if dp[i][j]:
            dp[i+1][j] = True
        elif j-t  >= 0 and dp[i][j-t]:
            dp[i+1][j] = True

ans = 10 ** 10

for i, row in enumerate(dp):
    for j, cell in enumerate(row):
        # print(i, j, cell)
        if j > 0 and cell:
            ans = min(ans, max(j, gokei - j))

print(ans)

# for row in dp:
#     for c in row:
#         if c:
#             print(1, end='')
#         else:
#             print(0, end='')
#     print()