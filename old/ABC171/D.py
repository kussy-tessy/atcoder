from collections import Counter

# print('input >>')
N = input()
As = list(map(int,(input().split())))
Q = int(input())
BCs = []
for _ in range(Q):
    BCs.append(tuple(map(int,(input().split()))))

counter = dict(Counter(As))
sum_ = sum(As)

for BC in BCs:
    if not BC[0] in counter:
        counter[BC[0]] = 0
    if not BC[1] in counter:
        counter[BC[1]] = 0
    sa = BC[1] - BC[0]
    sum_ += counter[BC[0]] * sa
    counter[BC[1]] = counter[BC[1]] + counter[BC[0]]
    counter[BC[0]] = 0
    # print(counter)
    print(sum_)