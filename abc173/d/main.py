#!/usr/bin/env python3

import heapq

N = int(input())
As = list(map(int,(input().split())))

# Aの大きい順に並べる
As.sort(reverse=True)

comf = [] # 心地よさ計算用
comf.append(-As[0]) # 最初の要素を追加(正負逆転)
heapq.heapify(comf)

ans = 0
for A in As[1:]: # 最初の要素は心地よさが0なので
    # print(comf)
    ans += -heapq.heappop(comf)
    # 2回pushする: その要素の端っこが新たな心地よさ候補となるため
    heapq.heappush(comf, -A)
    heapq.heappush(comf, -A)

print(ans)