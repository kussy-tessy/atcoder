import sys

# print('input >>')
N, K = map(int,(input().split()))
As = list(map(lambda x: int(x)-1,(input().split())))

visited = [0] * N
visited[0] = 1
roots = [0]
now = 0

# print('-----output-----')
while True:
    now = As[now]
    if visited[now] == 1:
        p = now
        rep_start = roots.index(now)
        move = len(roots) - rep_start
        break
    roots.append(now)
    visited[now] = 1

now = 0
if rep_start > K:
    for i in range(K):
        now = As[now]
    print(now+1)
    sys.exit()

# now = p
# for i in range(rep_start):
    # now = As[now]


K -= rep_start
K %= move
now = p

# print('K', K)
# print('now',now)

for i in range(K):
    now = As[now]

print(now+1)