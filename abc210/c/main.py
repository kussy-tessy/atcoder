#!/usr/bin/env python3

c_dict = {}

N, K = map(int,(input().split()))
cs = list(map(int,(input().split())))

ans = 0

for k in range(K):
    color = cs[k]
    if not color in c_dict:
        c_dict[color] = 0
    c_dict[color] += 1
    color_kinds = len(c_dict)
    ans = color_kinds

# print(c_dict)

for i in range(N-K):
    old_color = cs[i]
    c_dict[old_color] -= 1
    new_color = cs[i+K]
    if not new_color in c_dict:
        c_dict[new_color] = 0
    c_dict[new_color] += 1
    if c_dict[old_color] == 0:
        del c_dict[old_color]
    color_kinds = len(c_dict)
    ans = max(ans, color_kinds)
    # print(c_dict)

print(ans)