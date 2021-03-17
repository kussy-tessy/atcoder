from fractions import gcd

def lcm(x, y):
    return (x * y) // gcd(x, y)

# print('input >>')
A, B = map(int,(input().split()))

# print('-----output-----')
print(lcm(A, B))