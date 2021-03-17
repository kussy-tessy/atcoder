#!/usr/bin/env python3

from itertools import permutations
from sys import exit

N = input()
S = input()
rev = S[::-1]

pers = permutations(S, len(S))

for per in pers:
    per = ''.join(per)
    if not (per == S or per == rev):
        print(per)
        exit()

print('None')