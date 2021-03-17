import sys

# print('input >>')
A, R, N = map(int,(input().split()))

lar = 10**9

if R == 1:
    print(A)
    sys.exit()

for _ in range(N-1):
    A *= R
    if A > lar:
        print('large')
        sys.exit()

print(A)

# print('-----output-----')
