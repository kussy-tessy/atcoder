#!/usr/bin/env python3
from math import ceil

N, M = map(int,(input().split()))
As = list(map(int,(input().split())))

As.sort()

As = [0] + As
As += [N+1] 

# print(As)

As_diffs = [As[i+1] - As[i] - 1 for i in range(len(As)-1)]
As_diffs = [As_diff for As_diff in As_diffs if not As_diff == 0]
# print(As_diffs)

if len(As_diffs) == 0:
    print(0)
    import sys; sys.exit()

k = min(As_diffs)

ans = 0
for As_diff in As_diffs:
    ans += ceil(As_diff/k)

print(ans)