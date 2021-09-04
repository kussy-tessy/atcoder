#!/usr/bin/env python3
from collections import deque

N, M  = map(int,(input().split()))

Ms = []

for N in range(M):
    k = int(input())
    As = list(map(int,(input().split())))
    Ms.append(deque(reversed(As)))

def pop(dic):
    for dk, dv in dic.items():
        if len(dv) == 2:
            return (dk, dv)
    return None

dic = {}
for i, M in enumerate(Ms):
    if not M[0] in dic:
        dic[M[0]] = []
    dic[M[0]].append(i)

# print(dic)

while True:
    poped = pop(dic)
    if poped is None:
        print('No')
        exit()
    if poped == True:
        print('Yes')
        exit()
    popedk, popedv = poped
    popedv1, popedv2 = popedv
    Ms[popedv1].popleft()
    Ms[popedv2].popleft()
    del dic[popedk]
    if len(dic) == 0:
        print('Yes')
        exit()
    if len(Ms[popedv1]) > 0 and not Ms[popedv1][0] in dic:
        dic[Ms[popedv1][0]] = []
    dic[Ms[popedv1][0]].append(popedv1)
    if len(Ms[popedv2]) > 0 and not Ms[popedv2][0] in dic:
        dic[Ms[popedv2][0]] = []
    dic[Ms[popedv2][0]].append(popedv2)
    # print(dic)

"""
5 3
4
5 3 2 1
2
4 1
4
4 2 5 3
"""