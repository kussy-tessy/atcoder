#!/usr/bin/env python3

N = int(input())
Ps = list(map(int,(input().split())))
Q = int(input())
UDs = []
for _ in range(Q):
    UDs.append(tuple(map(int,(input().split()))))

childrens = [[] for _ in range(N)]
depth_dict = {}
parents = [[] for _ in range(N+1)]

for i, P in enumerate(Ps):
    parents[i+2] = [P] + parents[P]
    depth = len(parents[i+2])
    if not depth in depth_dict:
        depth_dict[depth] = [] 
    depth_dict[depth].append(i+2)
# print(depth_dict)
max_depth = max(depth_dict) 

# print(max_depth, 'max')
# print(parents)
for U, D in UDs:
    ans = 0
    if D > max_depth:
        print(0)
        continue
    cands = depth_dict[D]
    # print('cands', cands)
    # print('D', D, 'max_depth', max_depth)

    for cand in cands:
        # for c in parents[cand]:
        #     print('cand', cand, 'parents[cand]', parents[cand], 'c', c)
        #     if U in c:
        #         ans += 1
        # print('cand', cand)
        if U in [cand] + parents[cand]:
            ans += 1
        
    print(ans)

# 記念提出