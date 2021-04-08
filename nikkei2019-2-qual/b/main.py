#!/usr/bin/env python3
from collections import Counter

N = int(input())
Ds = list(map(int, input().split()))

Ds_coutner = Counter(Ds)
MOD = 998244353

# d=0が複数あると不可能
if Ds_coutner[0] >= 2:
    print(0)
    exit()
# 頂点1の距離が0なら不可能
if Ds[0] != 0:
    print(0)
    exit()

res = 1
for d in range(1, max(Ds_coutner)+1):
    prev_node_cnt = Ds_coutner[d-1]
    this_node_cnt = Ds_coutner[d]
    res *= prev_node_cnt ** this_node_cnt
    res %= MOD

print(res)