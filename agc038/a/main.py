#!/usr/bin/env python3

H, W, A, B = map(int,(input().split()))

for h in range(H):
    for w in range(W):
        if (h < B and w < A) or (h >= B and w >= A):
            print(0, end='')
        else:
            print(1, end='')
    print()