#!/usr/bin/env python3
from math import floor
from sys import exit

A, B, N = map(int,(input().split()))

# よくわからないので実験
# 周期性がある？

def calc(A, B, x):
    return floor(A * x / B) - A * floor(x / B)

"""prev_ans = 0
for x in range(N+1):
    ans = calc(A, B, x)
    if ans == 0:

    # if ans in answers:
    #     print(max(answers))
    #     exit()
    answers.add(ans)"""

# ans = 0
# for x in range(20):
#     print(x, calc(A, B, x))
#     ans = max(ans, calc(A, B, x))

# print(ans)

print(calc(A, B, min(B-1, N)))