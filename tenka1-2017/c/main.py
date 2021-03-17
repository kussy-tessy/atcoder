#!/usr/bin/env python3

N = int(input())

for h in range(1, 3500):
    for n in range(1, 3500):
        if (4*h*n - N*n - N*h) > 0:
            if (N*h*n) % (4*h*n - N*n - N*h) == 0:
                print(h, n, N*h*n // (4*h*n - N*n - N*h))
                exit()