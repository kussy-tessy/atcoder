#!/usr/bin/env python3

As = list(map(int,(input().split())))

As.sort()

if As[1] - As[0] == As[2] - As[1]:
    print('Yes')
else:
    print('No')