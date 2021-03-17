#!/usr/bin/env python3

from collections import Counter

S = input()

cs = Counter(S)
a = cs['a']
b = cs['b']
c = cs['c']

print('YES' if max(a,b,c) - min(a,b,c) <= 1 else 'NO')