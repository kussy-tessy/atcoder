#!/usr/bin/env python3

N, W = map(int,(input().split()))
STPs = []
for _ in range(N):
    STPs.append(tuple(map(int,(input().split()))))

waters = [0] * (2*10**5 + 5)

for (S, T, P) in STPs:
    waters[S] += P
    waters[T] -= P

now_water = 0
for water in waters:
    now_water += water
    if now_water > W:
        print('No')
        exit()

print('Yes')