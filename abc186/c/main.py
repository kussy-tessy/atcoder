#!/usr/bin/env python3

N = int(input())

ans = 0

for i in range(1, N+1):
    ten_ = str(i)
    oct_ = oct(i)[2:]
    ok = True
    for t in ten_:
        if t == '7':
            ok = False
            break
    if ok:
        for o in oct_:
            if o == '7':
                ok = False
                break
    if ok:
        ans += 1

print(ans)