


# print('input >>')
N, M = map(int,(input().split()))
ABs = [map(int,(input().split())) for _ in range(M)]

INF = 10 ** 10
ds = [INF] * (N+1)
marks = [0] * (N+1)

nodes = [None] * (N+1)

for AB in ABs:
    A, B = AB
    if nodes[A] is None:
        nodes[A] = []
    nodes[A].append(B)

    B, A = A, B
    if nodes[A] is None:
        nodes[A] = []
    nodes[A].append(B)

# print(nodes)

checked = [0] * (N+1) 

def dfs(cur, parent, children):
    print(cur, 'p', parent, children, 'c', checked)
    if checked[parent] == 1 and ds[parent] > cur:
        return
    checked[parent] = 1
    for child in children:
        print(parent, children, cur, ds)
        if ds[child] > cur:
            marks[child] = parent
            ds[child] = cur
            # print(marks)
        # if not checked[child] == 0:
        dfs(cur+1, child, nodes[child])

dfs(0, 1, nodes[1])

# print('-----output-----')
print('Yes')
for mark in marks[2:]:
    print(mark)

"""
7 7
1 2
2 5
5 7
3 1
7 3
6 1
2 4
"""