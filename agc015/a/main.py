#!/usr/bin/env python3

N, A, B = map(int,(input().split()))

# これらは問題（制約）の不備では……
if A > B:
    print(0)
    exit()
if N == 1 and A != B:
    print(0)
    exit()ac

print(B*(N-2) - A*(N-2) + 1)
