from collections import deque
import sys

# print('input >>')
N, X, Y = map(int, (input().split()))
shogais = set()

for _ in range(N):
    shogais.add(tuple(map(int,(input().split()))))

queue = deque()
now = ((0, 0), 0)
queue.append(now)
visited = set()
visited.add(now[0])

while queue:
    p = queue.popleft()
    pp = p[0] 
    pd = p[1]
    if pp == (X, Y):
        print(pd)
        sys.exit()
    for v in ((pp[0] + 1, pp[1] + 1), (pp[0], pp[1] + 1), (pp[0] - 1, pp[1] + 1), (pp[0] + 1, pp[1]), (pp[0] - 1, pp[1]), (pp[0], pp[1] - 1)):
        if -201 <= v[0] <= 201 and -201 <= v[1] <= 201: 
            if not v in shogais and not v in visited:
                visited.add(v)
                queue.append((v, pd + 1))

# print('----------output----------')
print(-1)