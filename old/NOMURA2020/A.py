# print('input >>')
H1, M1, H2, M2, K = map(int,(input().split()))

oki = H1 * 60 + M1
ne = H2 * 60 + M2

# print('-----output-----')
print(ne - oki - K)