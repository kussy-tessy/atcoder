import math
import sys

# print('input >>')
N = int(input())

if N % 2 == 1 or N == 0:
    print(0)
    sys.exit()

ans = 0
warusu = math.log(N, 5)
warusu = int(warusu)

for i in range(warusu):
    ans += (N // (5 ** (i+1))) // 2

# print('-----output-----')
print(ans)
