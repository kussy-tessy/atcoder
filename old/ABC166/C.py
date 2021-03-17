# print('input >>')
N, M = map(int,(input().split()))
H = list(map(int,(input().split())))
ABs = []
for _ in range(M):
    ABs.append(tuple(map(int,(input().split()))))

lists = [[] for _ in range(N)]

for AB in ABs:
    A, B = AB
    lists[A-1] += [H[B-1]]
    lists[B-1] += [H[A-1]]

ans = 0

for i, list_ in enumerate(lists):
    if all([H[i] > h for h in list_]) or len(list_) == 0:
        ans += 1

# print('-----output-----')
print(ans)