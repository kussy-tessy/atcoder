#!/usr/bin/env python3

K, T = map(int,(input().split()))
As = list(map(int,(input().split())))

# if len(As) == 1:
#     print(As[0] - 1)

As.sort()

As_max = As[-1]
As_other = sum(As[:-1])

print(max(0, As_max - As_other - 1))