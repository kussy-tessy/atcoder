print('input >>')
N, K = map(int,(input().split()))
Ps = [0] + list(map(int,(input().split())))
Cs = [0] + list(map(int,(input().split())))

visited = [0] * (N+1)
routes = []
for i in range(1, len(Ps)):
    if visited[Ps[i]] == 0:
        visited[i] = 1
        route = []
        start = i
        next_p = Ps[i]
        route.append(Cs[next_p])
        while True:
            visited[next_p] = 1
            next_p = Ps[next_p]
            route.append(Cs[next_p])
            if next_p == start:
                break
        routes.append(route)
        print('------')

for route in routes:
    ma = 0
    for r in routed:
        if r > 0:
            r > 

print('-----output-----')
print(routes)

# ここまでは考えたから！！！　記念提出！！