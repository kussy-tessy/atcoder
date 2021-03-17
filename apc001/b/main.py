#!/usr/bin/env python3

N = int(input())
As = list(map(int,(input().split())))
Bs = list(map(int,(input().split())))

t = 0
for A, B in zip(As, Bs):
    if A > B:
        t += B - A
    elif A < B:
        # if A % 2 == B % 2:
        t += (B - A) // 2
        # else:
            # t += (A - B) // 2

# print(t)

print('Yes' if t >= 0 else 'No')