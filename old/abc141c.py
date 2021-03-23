import collections

# print('input >>')
N, K, Q = map(int, (input().split()))
points = [K] * N
A = []
for _ in range(Q):
    A.append(int(input()))

Acount = collections.Counter(A)

for answerer, times in Acount.items():
    points[answerer - 1] += times

# print('----------output----------')

for answerer in range(N):
    print('Yes') if points[answerer] > Q else print('No')