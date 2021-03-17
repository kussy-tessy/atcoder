#!/usr/bin/env python3
N = int(input())
As = list(map(int,(input().split())))

up_or_down = None
prev = As[0]
cut = 0
for i in range(N):
    if up_or_down == 'up' and prev > As[i]:
        cut += 1
        # print(i)
        up_or_down = None
        prev = As[i]
        continue
    if up_or_down == 'down' and prev < As[i]:
        cut += 1
        # print(i)
        up_or_down = None
        prev = As[i]
        continue 
    if prev < As[i]:
        up_or_down = 'up'
    if prev > As[i]:
        up_or_down = 'down'
    prev = As[i]

print(cut+1)