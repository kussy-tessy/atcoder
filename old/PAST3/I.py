# print('input >>')
N = int(input())
Q = int(input())
queries = []

col = list(range(N+1))
row = list(range(N+1))

for _ in range(Q):
    queries.append(list(map(int,(input().split()))))

transpose = False

for q in queries:
    if q[0] == 1:
        A = q[1]
        B = q[2]
        if not transpose:
            row[A], row[B] = row[B], row[A]
        else:
            col[A], col[B] = col[B], col[A]
    if q[0] == 2:
        A = q[1]
        B = q[2]
        if not transpose:
            col[A], col[B] = col[B], col[A]
        else:
            row[A], row[B] = row[B], row[A]
    if q[0] == 3:
        transpose = not transpose
    if q[0] == 4:
        A = q[1]
        B = q[2]
        if not transpose:
            print(N * (row[A] - 1) + col[B] - 1)
        else:
            print(N * (row[B] - 1) + col[A] - 1)
    # print(row, col)

# print('-----output-----')