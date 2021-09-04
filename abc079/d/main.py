#!/usr/bin/env python3
import heapq

H, W = map(int,(input().split()))

cs = []
for _ in range(10):
    line = list(map(int,(input().split())))
    c = []
    for i, cost in enumerate(line):
        c.append((cost, i))
    cs.append(c)

As = []
for H in range(H):
    As.append(list(map(int,(input().split()))))

INF = 10**9

# for c in cs:
#     print(c)

def dijkstra(s):
    dist = [INF] * 10
    hq = [(0, s)] # (distance, node)

    dist[s] = 0
    visited = [False] * 10

    while hq:
        v = heapq.heappop(hq)[1]
        visited[v] = True
        for (cost, to) in cs[v]:
            if visited[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heapq.heappush(hq, (dist[to],to))

    return dist

costs = []
for i in range(10):
    costs.append(dijkstra(i))

ans = 0
for A_line in As:
    for A in A_line:
        if A != -1:
            ans += costs[A][1]

print(ans)