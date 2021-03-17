# print('input >>')
N, M, Q = map(int,(input().split()))

edges = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int,(input().split()))
    edges[u].append(v)
    edges[v].append(u)

colors = [0] + list(map(int,(input().split())))

ans = []

for _ in range(Q):
    query = list(map(int,(input().split())))
    if query[0] == 1:
        sp = query[1]
        ans.append(colors[sp])
        for s in edges[sp]:
            colors[s] = colors[sp]
    else:
        sp = query[1]
        color = query[2]
        ans.append(colors[sp])
        colors[sp] = color

# print('-----output-----')
for ans_ in ans:
    print(ans_)