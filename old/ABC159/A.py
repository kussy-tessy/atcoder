import math
import sys

def comb(n, r):
    if n <= 1:
        return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N, M = map(int,(input().split()))

print(comb(N,2) + comb(M,2))