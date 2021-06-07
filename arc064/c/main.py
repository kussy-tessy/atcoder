#!/usr/bin/env python3

N, x = map(int,(input().split()))

As = list(map(int,(input().split())))

ans = 0
for i in range(len(As) - 1):
    f = As[i]
    s = As[i+1]
    if f + s > x:
        ans += f + s - x
        s -= max(x - (f + s), s)
        if f + s > x:
            f -= x - s
    As[i] = f
    As[i + 1] = s
    
print(ans)