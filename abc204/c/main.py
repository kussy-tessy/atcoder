#!/usr/bin/env python3
from collections import deque

N, M = map(int,(input().split()))

ABs = []
rs = {i: [] for i in range(1, N+1)}

for _ in range(M):
    ABs.append(tuple(map(int,(input().split()))))

for A, B in ABs:
    rs[A].append(B)

# print(rs)
ans = 0

for i in range(1, N+1):
    stack = deque(rs[i])
    # print(f'{i}番目のstack', stack)
    g = set(stack)
    checked = set()
    while stack:
        leng = len(g)
        # if i==1:
        #     print('a', g)
        r = stack.pop()
        if r in checked:
            continue
        checked.add(r)
        # if i==1:
        #     print('b', r)
        if len(rs[r]) > 0:
            stack.extend(rs[r])
            # if i==1:
            #     print('c', rs[r], stack)
            g |= set(rs[r])
            # if i==1:
                # print(rs[r], g)
        # print(g)
        # if leng == len(g):
        #     break
        
    g.add(i)
    ans += len(g)
    # print(i, g)

print(ans)

"""
5 4
1 2
1 3
2 4
3 5
"""