def man_dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

# print('input >>')
N = int(input())
xys = []
for _ in range(N):
    xys.append(tuple(map(int,(input().split()))))

xys_x = sorted(xys, key=lambda xy: xy[0])
xys_y = sorted(xys, key=lambda xy: xy[1])

x_min = xys_x[0][0]
x_max = xys_x[-1][0]
y_min = xys_y[0][1]
y_max = xys_y[-1][1]

cand = [xy for xy in xys if xy[0] == x_min or xy[0] == x_max or xy[1] == y_max or xy[1] == y_min]

ans = 0

for c1 in cand:
    for c2 in cand:
        ans = max(ans, man_dist(c1, c2))

# print('-----output-----')
print(ans)