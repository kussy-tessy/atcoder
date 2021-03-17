#!/usr/bin/env python3

"""
def solve(x, n):
    return max(0, x - 2*n + 1)
"""

T = int(input())

cases = []

for _ in range(T):
    cases.append(tuple(map(int,(input().split()))))

for case in cases:
    L = case[0]
    R = case[1]
    ans = 0
    """for x in range(L, R+1):
        ans += solve(x, L)
    print(ans)"""
    # print((R-L+1)**2//2)
    if(R-L < L):
        print(0)
    else:
        print(int((R- 2*L + 2) * (-L + R/2 +1/2)))