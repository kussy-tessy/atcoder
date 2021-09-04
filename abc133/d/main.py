#!/usr/bin/env python3

N = int(input())
As = list(map(int,(input().split())))

gu = [A for (i, A) in enumerate(As) if i % 2 == 0]
ki = [A for (i, A) in enumerate(As) if i % 2 == 1]

x1 = sum(gu) - sum(ki)
x = x1
xs = [x]

for A in As[:-1]:
    xs.append(2*A - x)
    x = xs[-1]

print(' '.join([str(x) for x in xs]))