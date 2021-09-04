#!/usr/bin/env python3

N = int(input())
lrs = []
for _ in range(N):
    t, l, r = map(int,(input().split()))
    if t == 2:
        r -= 0.1
    elif t == 3:
        l += 0.1
    elif t == 4:
        l += 0.1
        r -= 0.1
    lrs.append((l, r))

lrs.sort(key=lambda lr:lr[0])
# print(lrs)

ans = 0

# for i in range(len(lrs)):
#     l = lrs[i][0]
#     r = lrs[i][1]
#     next_i = i+1
#     while next_i < N and lrs[next_i][0] <= r:
#         ans += 1
#         next_i += 1

for i in range(len(lrs)):
    l = lrs[i][0]
    r = lrs[i][1]
    for j in range(i+1, len(lrs)):
        jl = lrs[j][0]
        if l <= jl <= r:
            # print(i,j)
            ans += 1

print(ans)

# acc_sum = {}

# for (t, l, r) in tlrs:
#     if not l in acc_sum:
#         acc_sum[l] = 0
#     acc_sum[l] += 1
#     if not r+1 in acc_sum:
#         acc_sum[r+1] = 0
#     acc_sum[r+1] -= 1

# acc_sum_sorted = sorted(acc_sum.items(), key=lambda x:x[0])

# for 

# print(acc_sum_sorted)