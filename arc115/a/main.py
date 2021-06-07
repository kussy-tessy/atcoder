#!/usr/bin/env python3

N, M = map(int,(input().split()))
Ss = []
for _ in range(N):
    Ss.append(input())

odd_1 = 0

for S in Ss:
    cnt_1 = S.count('1') % 2 == 1
    if cnt_1:
        odd_1 += 1

print(odd_1 * (N-odd_1))
