from collections import Counter
import math

def comb(n):
    if n <= 1:
        return 0
    return n * (n-1) // 2

# print('input >>')
N = int(input())
A = list(map(int,(input().split())))

Ac = Counter(A)

sumc = 0

for Ae in dict(Ac):
    sumc += comb(Ac[Ae])

# print('-----output-----')

for k in A:
    print(sumc - comb(Ac[k]) + comb(Ac[k]-1))