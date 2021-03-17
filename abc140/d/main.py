#!/usr/bin/env python3

N, K = map(int,(input().split()))
S = input()

happy = 0

if N == 1:
    happy = 0
elif N == 2:
    if S == 'LL' or S == 'RR':
        happy = 1
    else:
        happy = 0
else:
    for i in range(1, N-1):
        if S[i] == 'R' and S[i+1] == 'R':
            # print(i, 'R')
            happy += 1
        if S[i] == 'L' and S[i-1] == 'L':
            # print(i, 'L')
            happy += 1
    if S[0] == 'R' and S[1] == 'R':
        happy += 1
    if S[-1] == 'L' and S[-2] == 'L':
        happy += 1
# print(happy)

# どうあがいても1回の操作で2人しか一度に幸福にできない
print(min(happy + 2*K, N-1))