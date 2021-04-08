#!/usr/bin/env python3

N = int(input())
S = input()

ans = ''
cacco = 0

for s in S:
    if s == '(':
        cacco += 1
    else:
        cacco -= 1
    ans += s
    if cacco < 0:
        ans = '(' + ans
        cacco += 1

if cacco > 0:
    ans += ')' * cacco

print(ans)