#!/usr/bin/env python3

N = int(input())

hit = set()
max_b = 0
for a in range(2, 10**5 + 5):
    for b in range(2, 40):
        if a ** b <= N:
            hit.add(a**b)
        else:
            break

print(N - len(hit))