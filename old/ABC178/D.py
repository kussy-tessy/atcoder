from math import factorial
from math import floor

def h(n, r):
    return factorial(n+r-1) // (factorial(n) * factorial(r-1))

# print('input >>')
S = int(input())
MOD = 10 **9 + 7

pattern_num = floor(S / 3)

ans = 0

for n in range(1, pattern_num+1):
    ans += h((S - 3*n), n)

# print('-----output-----')
print(ans % MOD)