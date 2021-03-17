#!/usr/bin/env python3
import heapq


N, M = map(int,(input().split()))
As = list(map(int,(input().split())))

# Mを分配してできるだけAが高い物に多めに割り振るという方針になりそうだけど、
# 総当りにする方法や計算方法などが分からん……
# ナイーブな貪欲では駄目で、なんらかの工夫が必要

# 解説……
# 割引券を使うたびにその時点で一番高い商品を選んで1回ずつ半額にするという操作を繰り返すのと等価

# Asが最大の値を返せるように-1をかける
As = [-A for A in As]

heapq.heapify(As)

for _ in range(M):
    max_A = -heapq.heappop(As)
    # print(max_A, max_A // 2)
    heapq.heappush(As, -(max_A // 2))
    # print(As)

ans = -sum(As)
print(ans)