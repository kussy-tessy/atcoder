#!/usr/bin/env python3
# 努力した記念提出

import math

X, Y, R = map(float,(input().split()))

def is_in_circle(x, y):
    return (x-X)**2 + (y-Y)**2 <= R**2

# https://twitter.com/meguru_comp/status/697008509376835584/photo/3
def count_lat_p(k):
    count = 0
    # left(円に初めて入る点)
    ok = math.floor(X - R)
    ng = math.floor(X) + 1
    print(k, 'l', ok, ng)
    while abs(ok - ng) > 1:
        mid = math.floor((ok + ng) / 2)
        if is_in_circle(mid, k):
            ok = mid
        else:
            ng = mid
    if not is_in_circle(mid, k):
        pts = 0
    else:
        pts = math.floor(X) + 1 - mid
    print(k, 'left', 'mid', mid)
    print(k, 'left', 'pts', pts)
    count += pts

    # right（円から初めて出る点）
    ok = math.ceil(X)
    ng = math.ceil(X + R) + 1
    print(k, 'r', ok, ng)
    while abs(ok - ng) > 1:
        mid = math.floor((ok + ng) / 2)
        if not is_in_circle(mid, k):
            ok = mid
        else:
            ng = mid
    if not is_in_circle(math.ceil(X), k):
        pts = 0
    else:
        pts = mid - math.ceil(X)
    print(k, 'right', 'mid', mid)
    print(k, 'right', 'pts', pts)
    count += pts
    return count

ans = 0
for k in range(math.floor(X-R), math.ceil(Y+R)):
    ans += count_lat_p(k)

print(ans)