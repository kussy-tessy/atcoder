#!/usr/bin/env python3

x, y = map(int,(input().split()))

xyz = set([0, 1, 2])

if len(set([x, y])) == 1:
    print(x)
else:
    print(list(xyz - set([x, y]))[0])