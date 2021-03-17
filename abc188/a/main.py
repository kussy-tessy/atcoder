#!/usr/bin/env python3
X, Y = map(int,(input().split()))

lose = min(X, Y)
win = max(X, Y)
if lose + 3 > win:
    print('Yes')
else:
    print('No')