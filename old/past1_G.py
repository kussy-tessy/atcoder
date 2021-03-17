def dfs(cur, kumi, x, happiness):
    if kumi == 1:
        x[cur] = 1
        for i, x_e in enumerate(x):
            if x_e == 1:
                happiness += G[i][cur]
    elif kumi == 2:
        x[cur] = 2
        for i, x_e in enumerate(x):
            if x_e == 2:
                happiness += G[i][cur]
    elif kumi == 3:
        x[cur] = 3
        for i, x_e in enumerate(x):
            if x_e == 3:
                happiness += G[i][cur]
    if cur == N-1:
        # print(x, happiness)
        return happiness
    _a = dfs(cur+1, 1, x, happiness)
    _b = dfs(cur+1, 2, x, happiness)
    _c = dfs(cur+1, 3, x, happiness)
    return max(_a, _b, _c)

N = int(input())
G = [[0] * N for _ in range(N)]

for i in range(N-1):
    info = list(map(int,(input().split())))
    for j in range(len(info)):
        G[i][i+j+1] = info[j]

a = dfs(0, 1, [0] * N, 0)
b = dfs(0, 2, [0] * N, 0)
c = dfs(0, 3, [0] * N, 0)

print(max(a, b, c))