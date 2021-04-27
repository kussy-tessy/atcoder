#!/usr/bin/env python3

N = int(input())
S = list(input())
Q = int(input())

queries = []
for _ in range(Q):
    queries.append(tuple(map(int,(input().split()))))

def true_pos_when_flip(x):
    if x <= N:
        return x + N
    else:
        return x - N

is_flip = False
for T, A, B in queries:
    if T == 1:
        if not is_flip:
            S[A-1], S[B-1] = S[B-1], S[A-1]
        else:
            S[true_pos_when_flip(A)-1], S[true_pos_when_flip(B)-1] = \
                S[true_pos_when_flip(B)-1], S[true_pos_when_flip(A)-1]
    if T == 2:
        is_flip = not is_flip

if not is_flip:
    print(''.join(S))
else:
    print(''.join(S[N:] + S[:N]))