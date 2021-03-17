#!/usr/bin/env python3

import bisect
import numpy as np

# 無理だああああ
# 記念提出
# 日数の制約条件がきつすぎ
# せめてbiのmaxが10**5ならいけた……

N, C = map(int,(input().split()))
abcs = []

for _ in range(N):
    abcs.append(tuple(map(int,(input().split()))))

events = {}
for (a, b, c) in abcs:
    if not a in events:
        events[a] = 0
    if not b+1 in events:
        events[b+1] = 0
    events[a] += c
    events[b+1] -= c

event_days = sorted(list(events.keys()))

total_cost = 0
day_cost = 0
prev_day = 0
now_plain_cost = 0
# print(events)
for day in event_days:
    total_cost += day_cost * (day-prev_day)
    cost_diff = events[day]
    day_cost = min(C, now_plain_cost + cost_diff)
    # print(f'{day=},{day_cost=}')
    now_plain_cost += cost_diff
    # print(f'{day_cost=},{day=},{prev_day=}')
    prev_day = day
print(total_cost)

"""
3 3
1 3 2
3 4 1
3 5 2
"""

"""
# costs = [0] * (10 ** 9 + 1)
costs = np.zeros(10 ** 9 + 1)
max_day = 0

for i in range(len(abcs)):
    a = abcs[i][0]
    b = abcs[i][1]
    c = abcs[i][2]
    max_day = max(max_day, b)
    costs[a] += c
    costs[b+1] -= c

costs = costs[:max_day+1]
for j in range(1, len(costs)):
    costs[j] += costs[j-1]

print(costs) 

# costs.sort()

# l = bisect.insort_left(costs, C)
# print()

# 3 4
# 2 4 5
# 4 5 2
# 1 2 3
"""