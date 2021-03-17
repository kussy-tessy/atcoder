import math
from functools import reduce
import itertools

def gcd(numbers):
    return reduce(math.gcd, numbers)

print('input >>')
K = int(input())

ans = 0
Ks = list(range(1, K+1))
lis = itertools.combinations_with_replacement(Ks, 3)

for li in lis:
    # print(list(li))
    # print(gcd(list(li)))
    ans += gcd(list(li))

print('-----output-----')
print(ans * 6)