from collections import Counter
from collections import deque

def cut_left(l, num):
    cut = {}
    while True:
        if not len(l) == 0:
            p = l.popleft()
            if not p[0] in cut:
                cut[p[0]] = 0
            if p[1] < num:
                cut[p[0]] += p[1]
                num -= p[1]
            else:
                l.appendleft((p[0], p[1]-num)) # ちょっと戻す
                cut[p[0]] += num
                break
        else:
            break

    ans = 0
    for v in cut.values():
        ans += v**2
    print(ans)

def append_to_right(l, char, num):
    l.append((char, num))

# print('input >>')
Q = int(input())
queries = []

for _ in range(Q):
    queries.append(input().split())

l = deque()

for query in queries:
    if query[0] == '1':
        append_to_right(l, query[1], int(query[2]))
    if query[0] == '2':
        cut_left(l, int(query[1]))

# print('-----output-----')