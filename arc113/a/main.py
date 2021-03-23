#!/usr/bin/env python3
# from collection import defaultdict
# import math

K = int(input())

ans = 0
for A in range(1, 2*10**5+1):
    for B in range(1, 2*10**5+1):
        ans += K // (A*B)
        if A * B >= K:
           break 
    if A > K:
        break
print(ans)