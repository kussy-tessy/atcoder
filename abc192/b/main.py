#!/usr/bin/env python3

S = input()

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
down = 'abcdefghijklmnopqrstuvwxyz'

is_yominikui = True

for i, s in enumerate(S):
    if i % 2 == 0 and s in upper: # 奇数
        is_yominikui = False
        break
    if i % 2 == 1 and s in down: # 偶数
        is_yominikui = False
        break

if is_yominikui:
    print('Yes')
else:
    print('No')