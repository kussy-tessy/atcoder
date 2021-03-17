from math import ceil

print('input >>')
N = int(input())
As = list(map(int,(input().split())))

ans = 0
# edge = As[-1]
edge = 0
lim = 2 ** N

for d in range(len(As)-1, -1, -1):
    edge += As[d]
    lim 
    if edge > lim:
        edge = ceil(edge/2)
        if edge > lim:
            print(-1)
    if d < N:
        ans += edge + As[d]
    # print(d, ans, edge)
    lim //= 2

# print('-----output-----')
print(ans)

# わからないけど撤退したわけではないというアピールのためにWAつけとく