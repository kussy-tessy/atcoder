#!/usr/bin/env python3
from collections import Counter

N, K = map(int,(input().split()))
As = list(map(int,(input().split())))

counter = Counter(As)

max_a = max(As)
final = []
now_b = counter[0] # 0が存在しない可能性あとで

for i in range(1, max_a + 2):
    b_diff = counter[i] - now_b
    if b_diff < 0:
        final.append((i, -b_diff))
    now_b = min(now_b, counter[i])

final.sort(key=lambda x: x[0], reverse=True)

ans = 0
box = 0
for final_ in final:
    num = final_[0]
    cnt = final_[1]
    if box + cnt <= K:
        ans += num * cnt
        box += cnt
    else:
        ans += num * (K - box)
        break

print(ans)

"""
20 4
1 1 1 1 1 2 2 3 3 3 3 4 4 4 4 5 5 5 5 5 5 5
"""