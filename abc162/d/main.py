#!/usr/bin/env python3

N = int(input())
S = input()

# 大まかな方針として余事象を考える

# 各文字の登場回数を調べる
r = S.count('R')
g = S.count('G')
b = S.count('B')

# S[i], S[j], S[k]がすべて異なるので、R,G,Bが異なる3箇所を選べばよい。
all_ptn = r * g * b

# i, j, kがR, G, Bが異なり、かつ等差数列となってしまっているパターンを調べる
ptn = 0
for i in range(N):
    for j in range(i, N):
        k = j + (j-i)
        if k >= N:
            break
        if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
            ptn += 1

print(all_ptn - ptn)

"""
R_idx = []
G_idx = []
B_idx = []

for i, s in enumerate(S):
    if s == 'R':
        R_idx.append(i)
    elif s == 'G':
        G_idx.append(i)
    elif s == 'B':
        B_idx.append(i)

# 全パターン丁寧に調べる

def cnt(idx1, idx2, idx3):
    res = 0
    for i in idx1:
        for j in idx2:
            if j > i:
                for k in idx3:
                    if k > j and k-j != j-i:
                        res += 1
    return res

ans = cnt(R_idx, G_idx, B_idx) + \
    cnt(R_idx, B_idx, G_idx) + \
    cnt(G_idx, R_idx, B_idx) + \
    cnt(G_idx, B_idx, R_idx) + \
    cnt(B_idx, R_idx, G_idx) + \
    cnt(B_idx, G_idx, R_idx)

print(ans)
"""