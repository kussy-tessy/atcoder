def distance(from_, to):
    return abs(from_[0]-to[0]) + abs(from_[1]-to[1])

# print('input >>')
N, M = map(int,(input().split()))
As = []
for _ in range(N):
    As.append(list(input()))

# 0番目は捨て
places = [[] for i in range(11)]

for i in range(N):
    for j in range(M):
        if not (As[i][j] == 'S' or As[i][j] == 'G'):
            places[int(As[i][j])].append([1000000,(i,j)])
        if As[i][j] == 'S':
            places[0] = [[0, (i, j)]]
        if As[i][j] == 'G':
            places[10] = [[10000000, (i, j)]]
# print('-----output-----')

for x in range(1, len(places)):
    # cost = [10000000] * len(places[x])
    for y in range(len(places[x])):
        for z in range(len(places[x-1])):
            # print(x, distance(places[x-1][z][1], places[x][y][1]))
            places[x][y][0] = min(places[x][y][0], places[x-1][z][0] + distance(places[x-1][z][1], places[x][y][1]))

ans = places[-1][0][0]

if ans > 100000:
    print(-1)
else:
    print(ans)