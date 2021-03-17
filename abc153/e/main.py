#!/usr/bin/env python3

H, N = map(int,(input().split()))
ABs = []

for _ in range(N):
    ABs.append(tuple(map(int,(input().split()))))

INF = 10 ** 9

# ダメージをi与えるのに必要な魔力
dp = [INF] * (H+1)
dp[0] = 0 # ダメージを与えていてないときは魔力も消費しない

for i, _ in enumerate(dp):
    # A: モンスターの体力、B: トキの魔力
    for j, (A, B) in enumerate(ABs):
        # dp[i]ははじめINFが入っていて記録が更新されるたびに書き換わる
        # 記録更新の対象は、ABsに入っているその魔法を使った場合の魔力
        # max(0, i-A)はインデクサがマイナスになったときの対策
        dp[i] = min(dp[i], dp[max(0,i-A)] + B)
        # print(i, j, dp)

print(dp[H])