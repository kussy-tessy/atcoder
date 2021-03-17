from collections import deque

print('input >>')
N, X, Y = map(int,(input().split()))
zahyo = [[0] * 10 for _ in range(10)]

for _ in range(N):
    x, y = map(int,(input().split()))
    zahyo[x][y] = -1

step = 0
now = [0, 0]
queue = deque([])
queue.append((0,0))

print(queue)

# while queue:
for i in range(100):
    p = queue.popleft()
    print(p)
    if [x, y] == [X, Y]:
        print(zahyo[X][Y])
        break
    for j, k in ([-1, 1], [1, 0], [1, 1], [-1, 0], [1, 0], [-1, 0]):
        new_x, new_y = x+j, y+k
        if not zahyo[new_x][new_y] > 0:
            zahyo[new_x][new_y] = zahyo[x][y] + 1
            queue.append((new_x, new_y))
            
print(zahyo)

print('-----output-----')