from math import sqrt
import sys

# print('input >>')
X = int(input())

if X == 1:
    print(0, -1)

for x in range(1, int(sqrt(X))):
    if X % x == 0:
        flg = False
        for a in range(1000000):
            if (a-1) ** 5 - (a-1-x) ** 5 < a ** 5 - (a-x) ** 5:
                flg = True
            if flg and a ** 5 - (a-x) ** 5 > X:
                break
            if a ** 5 - (a-x) ** 5 == X:
                print(a, a-x)
                sys.exit()

# print('-----output-----')
