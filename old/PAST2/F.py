import heapq

# print('input >>')
N = int(input())
tasks = [[] for i in range(N)]

for _ in range(N):
    day, point = map(int,(input().split()))
    tasks[day-1].append(-point)

can_task = []
heapq.heapify(can_task)

pnt = 0
for i in range(N):
    for p in tasks[i]:
        heapq.heappush(can_task, p)
    pnt += -heapq.heappop(can_task)
    print(pnt)

# print('-----output-----')