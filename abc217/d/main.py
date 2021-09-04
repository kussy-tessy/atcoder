#!/usr/bin/env python3
# import heapq
import bisect



L, Q = map(int,(input().split()))
ls = {}

for _ in range(Q):
    c, x = map(int,(input().split()))
    if c == 1:
        ls[x] = None
    else:
        