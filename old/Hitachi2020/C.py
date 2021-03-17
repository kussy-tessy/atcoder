from math import floor
import sys

# print('input >>')
A, B = map(int,(input().split()))

# print('-----output-----')
for i in range(20000):
    if floor(i * 0.08) == A and floor(i * 0.1) == B:
        print(i)
        sys.exit()

print('-1')
