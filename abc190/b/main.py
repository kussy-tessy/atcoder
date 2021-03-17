#!/usr/bin/env python3

N, S, D = map(int,(input().split()))
XYs = []
for _ in range(N):
    XYs.append(tuple(map(int,(input().split()))))

# can_damage = False

for XY in XYs:
    X = XY[0]
    Y = XY[1]
    if X < S and Y > D:
        # can_damage = True
        print('Yes')
        exit()

print('No')