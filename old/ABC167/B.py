import sys

# print('input >>')
A, B, C, K = map(int,(input().split()))

rest = K

if A >= K:
    print(K)
elif A+B >= K:
    print(A)
else:
    print(A+(-(K-A-B)))