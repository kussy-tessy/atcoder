#!/usr/bin/env python3

"""
C: 次の駅までかかる時間
S: 始発時刻
F: 発車間隔
"""

# xをaの倍数の大きい方に丸める
def ceiling(x, a):
    return x + -x % a

N = int(input())
CSFs = []
for _ in range(N-1):
    CSFs.append(tuple(map(int,(input().split()))))

for i in range(len(CSFs)):
    start = CSFs[i][1]
    time = start
    for j in range(i, len(CSFs)):
        first_train = CSFs[j][1]
        interval = CSFs[j][2]
        next_time = max(first_train, ceiling(time, interval))
        duration = CSFs[j][0]
        time = next_time + duration
    print(time)
print(0)