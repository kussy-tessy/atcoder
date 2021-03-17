#!/usr/bin/env python3
from heapq import heappush, heappop

# 指定された値の倍数となるように切り上げる - Qiita
# https://qiita.com/cress_cc/items/f333a54619f5cb480eb0

def ceiling(v, n):
    return v + -v % n

N, M, X, Y = map(int,(input().split()))
# N: ノード
# M: エッジ
# X: スタート
# Y: ゴール
# https://mirucacule.hatenablog.com/entry/2020/05/21/124026
# adj[s]: ノードsに隣接する(ノード, 時間, 発車間隔)をリストで持つ
adj = [[] for _ in range(N+1)]
for _ in range(M):
    A, B, T, K = map(int,(input().split()))
    adj[A].append((B, T, K))
    adj[B].append((A, T, K))

# ダイクストラ的なあれ
INF = float('inf')
dist = [INF] * (N+1) # dist[s]: ノードsへの最短到達時間
hq = [(0, X)] # (時刻, ノード)を管理するヒープ
dist[X] = 0
# seen = [False] * (N+1)
while hq:
    v_dist, v_node = heappop(hq) # ノードをpopする
    # seen[v_node] = True
    for to, time, interval in adj[v_node]: # 隣接しているノードに対して
        plus_time = ceiling(v_dist, interval) + time
        # if seen[to] == False and plus_time < dist[to]:
        if plus_time < dist[to]:
            dist[to] = min(dist[to], plus_time)
            heappush(hq, (dist[to], to))

# print(dist)
print(dist[Y] if dist[Y] != INF else -1)

"""
3 2 1 3
1 2 2 3
2 3 5 4
"""