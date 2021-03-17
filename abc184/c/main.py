#!/usr/bin/env python3
from math import ceil

r1, c1 = map(int,(input().split()))
r2, c2 = map(int,(input().split()))

"""
# とりあえず斜めで行けるとこまで行く
r1_n, c1_n = max(r2, c2), max(r2, c2)

# 横に移動
diff = r1_n - min(r2, c2)

times = ceil(diff / 3)

print(1 + times)
"""

if r1 == r2 and c1 == c2:
    print(0)
elif abs(r2 - r1) == abs(c2 - c1):
    print(1)
elif abs(r2-r1) + abs(c2-c1) <= 3:
    print(1)
elif (abs(r2-r1) + abs(c2-c1)) % 2 == 0:
    print(2)
elif abs(abs(r2 - r1) - abs(c2 - c1)) <= 3:
    print(2)
elif abs(r2-r1)+abs(c2-c1) <= 6:
    print(2)
else:
    print(3)

# 解説ACを目指す
