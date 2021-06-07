#!/usr/bin/env python3

N, M = map(int,(input().split()))
xys = []
for _ in range(M):
    xys.append(tuple(map(int,(input().split()))))

ball = [1] * (N+1)
ball[0] = 0

p = [0] * (N+1)
p[1] = 1

for x, y in xys:
    ball[x] -= 1
    ball[y] += 1
    if p[x] == 1 > 0:
        p[y] = 1
        if ball[x] == 0:
            p[x] = 0

# print(ball)
# print(p)

print(sum(p))