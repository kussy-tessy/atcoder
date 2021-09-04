#!/usr/bin/env python3

N = int(input())
# N = 10**9

n = lambda i: i*(i+1) / 2

for i in range(100000):
    if n(i) >= N:
        print(i)
        exit()