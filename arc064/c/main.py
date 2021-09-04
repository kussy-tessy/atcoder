#!/usr/bin/env python3
 
N, x = map(int,(input().split()))
 
As = list(map(int,(input().split())))
 
ans = 0

for i in range(len(As) - 1):
    f = As[i]
    s = As[i+1]
    if f + s > x:
        ans += f + s - x
        s = max(0, s-(f+s-x))
    As[i + 1] = s

print(ans)