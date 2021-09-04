#!/usr/bin/env python3

N = int(input())

As = list(map(int,(input().split())))

As.sort()

for i, A in enumerate(As):
    if i+1 != A:
        print('No')
        exit()

print('Yes')