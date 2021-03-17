import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

# print('input >>')
K = int(input())

ans = 0
for a in range(1, K+1):
    for b in range(1, K+1):
        for c in range(1, K+1):
            ans += gcd(a, b, c)

# print('-----output-----')
print(ans)