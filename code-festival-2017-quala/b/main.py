#!/usr/bin/env python3

N, M, K = map(int,(input().split()))

def calc_K(n, m):
    return (n * (M - m))+((N - n) * m)

for n in range(N+1):
    for m in range(M+1):
        # print(f'{n=}{m=}k={calc_K(n, m)}')
        if calc_K(n, m) == K:
            print('Yes')
            exit()

print('No')