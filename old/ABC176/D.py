from collections import deque

print('input >>')
H, W = map(int,(input().split()))
Ch, Cw = map(int,(input().split()))
Dh, Dw = map(int,(input().split()))

grid = []
for _ in range(H):
    grid.append(input())

search = [[0] * W for _ in range(H)]

# for i in range(H):
#     for j in range(W):

q = []
q = deque(q)

q.append((Ch, Cw, 0))
while q:
    v = q.popleft()
    vh = v[0]
    vw = v[1]
    wall = v[2]
    for i in range(-2, 3):
        for j in range(-2, 3):
            try:
                if grid[vh+i][vw+j] == '.':
                    search[vh+i][vw+j] = wall + 1
            except:
                pass
    for t in ((vh+1, vw), (vh, vw+1), (vh-1, vw), (vh, vw-1)):


print('-----output-----')
# 記念提出