#!/usr/bin/env python3

N = int(input())
S = input()

for (i, s) in enumerate(S):
    if i % 2 == 0 and s == '1': # takahashi
        print('Takahashi')
        exit()
    if 1 % 2 == 1 and s == '1': # aoki
        print('Aoki')
        exit()

