from math import ceil

# print('input >>')
N, X, T = map(int,(input().split()))

# print('-----output-----')
print(ceil(N / X) * T)