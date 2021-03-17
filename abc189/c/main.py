#!/usr/bin/env python3

N = input()
As = list(map(int,(input().split())))

"""
ans = 0
for i in range(len(As)):
    for j in range(i, len(As)):
        # print(i, As[i], j, As[j])
        if As[j] < As[i]:
            ans = max(ans, As[i] * (j-i))
            # print(ans)
            break
        if j == len(As)-1:
            # print('ok')
            ans = max(ans, As[i] * (len(As)-i))


print(ans)
"""
ans = 0
for i in range(len(As)):
    for left in range(i, -1, -1):
        if As[left] < As[i]:
            l_bound = left + 1
            break
        if left == 0:
            l_bound = 0
    for right in range(i, len(As), 1):
        if As[right] < As[i]:
            r_bound = right - 1
            break
        if right == len(As) - 1:
            r_bound = len(As) - 1
    # print(i, l_bound, r_bound)
    ans = max(ans, As[i] * (r_bound - l_bound + 1))

print(ans)


"""
ans = 0
# これ普通にPythonで間に合う？？？
for i in range(len(As)):
    x = As[i]
    for j in range(i, len(As)):
        x = min(x, As[j])
        ans = max(ans, x * (j-i+1))

print(ans)
"""