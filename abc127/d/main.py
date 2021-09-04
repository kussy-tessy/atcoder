#!/usr/bin/env python
import bisect

N, M = map(int,(input().split()))
As = list(map(int,(input().split())))
As.sort()
BCs = []
for _ in range(M):
    BCs.append(tuple(map(int,(input().split()))))
BCs.sort(key=lambda BC:BC[1], reverse=True)

i = 0
# Cという数字にB枚書き換える
B, C = list(BCs[0])

ans = 0
for A in As:
    # print(f'{A=}, {BCs=}, {B=}, {C=}, {ans=}')
    if B == 0:
        # BCs = BCs[1:]
        # print(f'{i=}')
        if i < len(BCs)-1:
            i += 1
            B, C = BCs[i]
        else:
            ans += A
            continue
    if A < C:
        ans += C
        B -= 1
    else:
        ans += A

print(ans)

"""
As.sort()
A_front = {}
cut_idx = 0
# cut_A = As.copy()
BCs.sort(key=lambda BC:BC[1], reverse=True)
print(f'{As=}')

before_b = 0
for B, C in BCs:
    print(f'{B=}, {C=}')
    # if before_b < B:
    idx = bisect.bisect(As, C)
    print(f'{idx=}')
    if idx > 0:
        max_idx = min(cut_idx+idx, cut_idx+B)
        print(f'{C=}')
        A_front[C] = max_idx
        As = As[max_idx:]
        cut_idx += max_idx
    # before_b = B
    print(A_front, As)

ans = 0
for num, cnt in A_front.items():
    ans += num * cnt

for a in As:
    ans += a

print(ans)
"""