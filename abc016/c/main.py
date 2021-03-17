#!/usr/bin/env python3

N, M = map(int,(input().split()))

fs = {}

for i in range(1, N+1):
    fs[i] = []

for i in range(M):
    A, B = map(int,(input().split()))
    fs[A].append(B)
    fs[B].append(A)

# print(fs)

for i in range(1, N+1):
    friends = fs[i]
    fr_of_frs = set()
    for friend in friends:
        fr_of_the_frs = fs[friend]
        for f in fr_of_the_frs:
            if not f in fs[i] and not f == i: # 自分の友だちでないかつ自分でない
                fr_of_frs.add(f)
    print(len(fr_of_frs))