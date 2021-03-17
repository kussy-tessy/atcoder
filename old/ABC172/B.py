# print('input >>')
N, D = map(int,(input().split()))
XYs = []
for _ in range(N):
    XYs.append(tuple(map(int,(input().split()))))

ans = 0

for XY in XYs:
    X = XY[0]
    Y = XY[1]
    dist = X ** 2 + Y ** 2
    if dist <= D ** 2:
        ans += 1

# print('-----output-----')

print(ans)