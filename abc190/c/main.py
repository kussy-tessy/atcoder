#!/usr/bin/env python3


N, M = map(int,(input().split()))
ABs = []
for _ in range(M):
    ABs.append(tuple(map(int,(input().split()))))
K = int(input())
CDs = []
for _ in range(K):
    CDs.append(tuple(map(int,(input().split()))))

def cnt_cond(cnts):
    cnt = 0
    for A, B in ABs:
        if cnts[A] > 0 and cnts[B] > 0:
            cnt += 1
    return cnt

def dfs(cnts, dish, cur):
    cnts[dish] += 1
    if cur == K-1:
        # print(cnt_cond(cnts))
        return cnt_cond(cnts)
    else:
        return max(dfs(cnts.copy(), CDs[cur+1][0], cur + 1), dfs(cnts.copy(), CDs[cur+1][1], cur + 1))

print(max(dfs([0] * (N+1), CDs[0][0], 0), dfs([0] * (N+1), CDs[0][1], 0)))