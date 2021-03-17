from fractions import gcd
from functools import reduce

mod = 10 ** 9 + 7

def lcm_base(x, y):
    return (x * y) // gcd(x, y)

def lcm(numbers):
    return reduce(lcm_base, numbers, 1)

# print('input >>')
N = int(input())
A = list(map(int,(input().split())))

lcmn = lcm(A)

ans = 0
for i in range(len(A)):
    ans += lcmn // A[i]

# print('-----output-----')
print(int(ans%mod))