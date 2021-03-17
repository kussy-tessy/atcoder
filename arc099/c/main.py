#!/usr/bin/env python3
from math import ceil

"""N, K = map(int,(input().split()))
As = list(map(int,(input().split())))"""

# コーナーケースがわからん
def solve1(N, K):
    if K == N:
        return(1)
    elif K == 2:
        return(N-1)
    else:
        return(ceil(N / (K-1)))

def solve2(N, K):
    return (ceil((N-1)/(K-1)))

for N in range(2, 100):
    for K in range(2, 100):
        if solve1(N, K) != solve2(N, K):
            print(f'{N=},{K=}で食い違う！')