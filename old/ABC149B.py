# print('input >>')
A, B, K = map(int,(input().split()))

# print('-----output-----')
if K < A:
    print(A-K, B)
elif K < (A + B):
    print(0, (A+B)-K)
else:
    print(0, 0)