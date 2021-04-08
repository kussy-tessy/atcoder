#!/usr/bin/env python3

N = int(input())
# N = 10**7

def get_i(N):
    my_sum = 0
    i = 0
    while my_sum < N:
        i += 1
        my_sum += i
    return i

solve_p = []
while N >= 1:
    p = get_i(N)
    solve_p.append(p)
    N -= p

for solve_p_ in solve_p:
    print(solve_p_)
# print(i, my_sum)