import math
from functools import reduce

# def gcd(*numbers):
    # return reduce(math.gcd, numbers)

# def gcd_list(numbers):
    # return reduce(math.gcd, numbers)

def lcm(x, y, my_gcd):
    return (x * y) // my_gcd

# print('input >>')
N = input()
As = list(map(int,(input().split())))
As.sort()

my_gcd = As[0] 
GCD = my_gcd
my_lcm = As[0]
has_pair = False

for i in range(1, len(As)):
    GCD = math.gcd(GCD, As[i])
    if not has_pair:
        LCM = lcm(my_lcm, As[i], GCD)
        if LCM != my_lcm * As[i]:
            has_pair = True

# print('-----output-----')
if GCD == 1 and not has_pair:
    print('pairwise coprime')
elif GCD == 1 and has_pair:
    print('setwise coprime')
else:
    print('not coprime')