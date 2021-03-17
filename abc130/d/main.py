#!/usr/bin/env python3

N, K = map(int,(input().split()))
As = list(map(int,(input().split())))

# 尺取法まじでわからんので写経する
r = 0 # 右端
ans = 0 # 答え
gokei = 0 # 区間和
for l in range(N): # lを左端から動かしながら調べていく
    while r < N and gokei < K: # r < Nの範囲内で(rが右端にくっついたらbreak)、区間和がK未満である間は
        gokei += As[r] # 区間和に右端の値を足す
        r += 1 # 右端を動かす
    if gokei < K: # rが右端ににくっついても区間和がK未満であるとき
        break # そのlについては調べても意味がないので調査打ち切り
    ans += N - r + 1 # そのlにおいて[l, r]が最小の条件を満たす区間和。rがそれより右の範囲はすべて条件を満たす
    gokei -= As[l] # 次のlの区間和では左端の値はもういないので引いておく
print(ans)

"""
# print(As_sum)
ans = 0
r = N-1
# gokei = As_sum[-1]
gokei = sum(As)
for l in range(N):
    while r < N-1 and gokei + As[r] < K:
        r += 1
    while r > 0 and gokei - As[r] >= K:
        print(l, r)
        gokei -= As[r]
        r -= 1
    ans += N - r + 1
    if r == l:
        r += 1
    else:
        gokei -= As[l]
    
    
print(ans)
"""

"""
尺取法
r = 0
gokei = 0
res = 0

for l in range(len(As)):
    p = 0
    while r < N and gokei + As[r] < K:
        gokei += As[r]
        r += 1
        p += 1
    res += p
    if r == l:
        r += 1
    else:
        gokei -= As[l]

print(int(N*(N-1) / 2) - res)
"""