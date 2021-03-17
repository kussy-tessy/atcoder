#!/usr/bin/env python3

N, K = map(int,(input().split()))
As = list(map(lambda x:int(x)-1,(input().split())))

visited_time = [0] * len(As)
visited_time[0] = 1

i = 1
d = 0

while True:
    next_d = As[d]
    i += 1
    # print(i, visited_time)
    if visited_time[next_d] == 0:
        visited_time[next_d] = i
        d = next_d
    else:
        tail = visited_time[next_d] - 1
        cyc = i - tail - 1
        # print(tail, cyc)
        break


if K <= (tail + cyc -1):
    print(visited_time.index(K+1)+1)
else:
    Kcyc = K - tail
    Kcycmod = Kcyc % cyc
    # print(Kcycmod+tail, '探す')
    print(visited_time.index(Kcycmod+tail+1)+1)

