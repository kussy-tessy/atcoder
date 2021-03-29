#!/usr/bin/env python3

N, K = map(int,(input().split()))
As = list(map(int,(input().split())))
MOD = 10**9 + 7

# [(前で転倒数, 後ろで転倒数)]
cnts = [None] * N

for i, A in enumerate(As):
    front = 0
    back = 0
    for j, Aj in enumerate(As):
        if j < i and Aj < A:
            front += 1
        elif j > i and Aj < A:
            back += 1
    cnts[i] = (front, back)

# print(cnts)
ans = 0
for (front, back) in cnts:
    ans += back * K + back * K*(K-1) // 2 + front * K*(K-1) // 2
    ans %= MOD
    # print(ans)

print(ans)