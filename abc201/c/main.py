#!/usr/bin/env python3
from collections import Counter

S = input()

ans = 0
for i in range(10000):
    i_str = str(i).zfill(4)
    i_str_counter = Counter(i_str)
    is_ok = True
    for x in range(10):
        if S[x] == 'o' and i_str_counter[str(x)] == 0:
            is_ok = False
            break
        if S[x] == 'x' and i_str_counter[str(x)] > 0:
            is_ok = False
            break
    if is_ok:
        ans += 1

print(ans) 