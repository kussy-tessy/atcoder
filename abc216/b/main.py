#!/usr/bin/env python3

N = int(input())
names = set()

for _ in range(N):
    names.add(input())

if len(names) == N:
    print('No')
else:
    print('Yes')