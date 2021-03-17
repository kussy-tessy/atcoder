#!/usr/bin/env python3

K = int(input())
S = input()
T = input()

def calc_score(S):
    cnts = [0] * 10
    for s in S:
        cnts[int(s)] += 1
    score = 0
    for i, cnt in enumerate(cnts):
        score += i * 10**cnt
    return score

# cnts: dict
def calc_possibility(cnts, A, B):
    all_cnt = 0
    for i, cnt in cnts.items():
        all_cnt += cnt
    all_pattern = all_cnt * (all_cnt - 1)
    A_cnt = cnts[str(A)]
    cnts[str(A)] -= 1
    B_cnt = cnts[str(B)]
    target_pattern = A_cnt * B_cnt
    return target_pattern / all_pattern

origin_cnts = {str(i): K for i in range(1, 10)}
# print(origin_cnts)

for a in S[:-1]:
    origin_cnts[a] -= 1
for b in T[:-1]:
    origin_cnts[b] -= 1

possibility = 0
for i in range(1, 10):
    for j in range(1, 10):
        S_p = S[:-1] + str(i)
        T_p = T[:-1] + str(j)
        if calc_score(S_p) > calc_score(T_p):
            cnts = origin_cnts.copy()
            possibility += calc_possibility(cnts, i, j)

print(possibility)