#!/usr/bin/env python3

N = int(input())
ABs = []

for _ in range(N):
    ABs.append(tuple(map(int,(input().split()))))

ABs_cal = [(-AB[0], AB[0]+AB[1]) for AB in ABs]
now_A = sum([AB[0] for AB in ABs])

ABs_cal.sort(key=lambda AB: AB[1] - AB[0], reverse=True)

i = 0
now_B = 0
while not now_B > now_A:
    now_A += ABs_cal[i][0]
    now_B += ABs_cal[i][1]
    i += 1

print(i)