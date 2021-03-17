from collections import deque

# print('input >>')
N, M = map(int,(input().split()))
ABs = [map(int,(input().split())) for _ in range(M)]

INF = 10 ** 10
ds = [INF] * (N+1)
marks = [0] * (N+1)

nodes = [None] * (N+1)

for AB in ABs:
    A, B = AB
    if nodes[A] is None:
        nodes[A] = []
    nodes[A].append(B)

    B, A = A, B
    if nodes[A] is None:
        nodes[A] = []
    nodes[A].append(B)

# print(nodes)

queue = deque([1])
visited = [0] * (N+1)
visited[1] = 1

# d = 0
# ds = [INF] * (N+1)
marks = [0] * (N+1)
parent = 1

while len(queue) > 0:
    p = queue.popleft()
    # print(p)
    # parent, node = p[0], p[1]
    # visited[node] = 1
    # marks[node] = parent
    for n in nodes[p]:
        if visited[n] == 0:
            visited[n] = 1
            marks[n] = p
            queue.append(n)

print('Yes')
for mark in marks[2:]:
    print(mark)
