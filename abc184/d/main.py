#!/usr/bin/env python3

A, B, C = map(int,(input().split()))

# 無理だったけどもったいないのでsubmitします。。。
def dfs(A, B, C, depth, prob):
    print(A, B, C, depth, prob)
    if max(A, B, C) == 100:
        return depth * prob
    return dfs(A+1, B, C, depth+1, prob*A/(A+B+C)) + \
         dfs(A, B+1, C, depth+1, prob*B/(A+B+C)) + \
         dfs(A, B, C+1, depth+1, prob*C/(A+B+C))

print(dfs(A, B, C, 0, 1)) 
