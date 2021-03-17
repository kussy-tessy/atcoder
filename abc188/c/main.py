#!/usr/bin/env python3

import sys

N = int(input())
As = list(map(int,(input().split())))

now = As

if(len(As) == 2):
    print(As.index(min(As))+1)
    sys.exit()

while len(now) > 2:
# for j in range(5):
    next_ = []
    for i in range(0, len(now), 2):
        # print(i)
        next_.append(max(now[i], now[i+1]))
    now = next_
# print(next_)

winner_rate = min(next_)
print(As.index(winner_rate)+1)