from math import factorial

INF = 10 ** 9 + 7
fact = [0]

def comb(n, r):
    return factorial(n) // (factorial(n-r) * factorial(r))

print(9*6%13)
print('input >>')
n, a, b = map(int,(input().split()))



print('-----output-----')

print(all % INF)


