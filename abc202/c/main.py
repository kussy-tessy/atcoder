#!/usr/bin/env python3

# from collections import Counter

N = int(input())

As = list(map(lambda x:int(x)-1,(input().split())))
Bs = list(map(lambda x:int(x)-1,(input().split())))
Cs = list(map(lambda x:int(x)-1,(input().split())))

As_idxs = [[] for _ in range(N)]
Bs_idxs = [[] for _ in range(N)]
Cs_idxs = [[] for _ in range(N)]

for i, A in enumerate(As):
    As_idxs[A].append(i+1)
for i, B in enumerate(Bs):
    Bs_idxs[B].append(i+1)
for i, C in enumerate(Cs):
    Cs_idxs[C].append(i+1)

# print(As_idxs)
# print(Bs_idxs)
# print(Cs_idxs)
ans = 0
for a, As_idx in enumerate(As_idxs):
    b = Bs_idxs[a] # aという数字がどこにある
    for b_ in b:
        ans += len(As_idx) * len(Cs_idxs[b_-1])
print(ans)

"""
# Bs_counter = Counter(Bs)
Bs_dict = {}
Cs_counter = Counter(Cs)

for i, B in enumerate(Bs):
    if not B in Bs_dict:
        Bs_dict[B] = []
    Bs_dict[B].append(i)

ans = 0
for A in As:
    if not A in Bs_dict:
        continue 
    indices = Bs_dict[A]
    for idx in indices:
        ans += Cs_counter[idx]

print(ans)
"""

