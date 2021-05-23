#!/usr/bin/env python3

N = int(input())

STs = []
for _ in range(N):
    S, T = input().split()
    T = int(T)
    STs.append((S, T))

STs.sort(key=lambda ST:ST[1], reverse=True)

print(STs[1][0])