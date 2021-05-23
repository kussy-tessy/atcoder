#!/usr/bin/env python3

N, M, Q = map(int,(input().split()))
WVs = []
for _ in range(N):
    WVs.append(tuple(map(int,(input().split()))))
Xs = list(map(int,(input().split())))
WVs.sort(key=lambda wv:wv[1], reverse=True)
# Xs.sort()

def calc(boxes):
    # print(boxes)
    boxes.sort()
    val = 0
    used = [0] * len(boxes)
    # print(boxes)
    for W, V in WVs:
        # print(f"大きさ{W}、価値{V}の品物について考える")
        for i, X in enumerate(boxes):
            # print(f"容積{X}の箱には……")
            if X >= W and not used[i]:
                # print(f"入るので入れる！")
                val += V
                used[i] = 1
                break
    return val

for _ in range(Q):
    L, R = map(int,(input().split()))
    boxes = Xs[:L-1] + Xs[R:]
    print(calc(boxes))

# print("a", Xs[:0])