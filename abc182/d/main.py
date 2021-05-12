#!/usr/bin/env python3

# 分からんので愚直解を考える
N = int(input())
As = list(map(int,(input().split())))

# https://drken1215.hatenablog.com/entry/2020/11/30/031357
# 累積和とその時点でのMAX（一番右に行ける量）を持つ
# i回目の操作を終えたときの位置を確認していく

As_imos = [0] * len(As)
As_imos[0] = As[0]
As_max = [0] * len(As)
As_max[0] = max(As[0], 0)

ans = 0
p = As[0]
for i in range(1, len(As)):
    # print(p)
    As_imos[i] += As_imos[i-1] + As[i]
    As_max[i] = max(As_max[i-1], As_imos[i])
    ans = max(ans, p+As_max[i])
    p += As_imos[i]

# print(As_imos)
# print(As_max)

print(max(ans, As[0]))


# ans = -float('inf')
# pos = 0
# ans = 0

# for i, A in enumerate(As):
#     print('----')
#     for j in range(i+1):
#         pos += As[j]
#         print(pos)
#         ans = max(ans, pos)

# # print(ans)

# As_imos = [0] * len(As)
# As_imos[0] = As[0]
# for i in range(1, len(As)):
#     As_imos[i] = As_imos[i-1] + As[i]

# ans = 0
# l = 0
# for i in range(len(As)):
#     if i == 0:
#         l += As[i]
#     else:
#         l += As_imos[i-1] + As[i]
#     # print(l)
#     print(ans, ans+As_imos[i-1], l, As_imos[i])
#     ans = max(ans+As_imos[i-1], ans, l)

# print(ans)