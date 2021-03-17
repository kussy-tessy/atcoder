from math import floor, ceil
import sys

# print('input >>')
N = int(input())
matrix = []

for _ in range(N):
    matrix.append(input())

to_num = lambda char: ord(char)-97
to_char = lambda num: chr(num+97)
matrix_s = [[0] * 26 for _ in range(N)]

# print(matrix_s)

for i, matri in enumerate(matrix):
    for matr in matri:
        # print(i, matr, to_num(matr))
        matrix_s[i][to_num(matr)] += 1

ans = []

for j in range(N):
    for p, (x, y) in enumerate(zip(matrix_s[j], matrix_s[N-1-j])):
        if x > 0 and y > 0:
            ans.append(to_char(p))
            break

if N == 1:
    print(matrix[0][0])
    sys.exit()

# print(ans)

if len(ans) < N:
    print(-1)
else:
    for ans_ in ans:
        print(ans_, end='')

# print('-----output-----')