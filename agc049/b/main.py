#!/usr/bin/env python3
from collections import deque

N = int(input())
S = input()
T = input()

diffs = deque()
ans = 0

for i in range(N):
    if S[i] == '0' and T[i] == '1':
        # S[i] == 0, T[i] == 1のときはどうしようもない
        diffs.append(i)
    if S[i] == '1' and T[i] == '0':
        # S[i] == 1, T[i] == 0のときは最寄りの違ったインデックスまで移動させるコストがかかる
        if diffs:
            ans += i - diffs.popleft()
        else:
            diffs.append(i)
    # print(f"{diffs=}")
if diffs:
    print(-1)
else:
    print(ans)            