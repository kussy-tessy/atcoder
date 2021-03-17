#!/usr/bin/env python3

S = input()

lenS = len(S)

res = 0

for i in range(lenS):
    if S[i] == 'U':
        res += i * 2 + (lenS-i-1) * 1
    elif S[i] == 'D':
        res += i * 1 + (lenS-i-1) * 2

print(res) 