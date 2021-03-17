from decimal import *

# print('input >>')
A, B = input().split()

ans = Decimal(A) * Decimal(B)
# ans = A * 100 * B * 100 / 10000

# print('-----output-----')
print(int(ans))