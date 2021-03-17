# print('input >>')
A, B, C = map(int,(input().split()))
K = int(input())

for _ in range(K):
    if B >= C:
        C *= 2
    elif A >= B:
        B *= 2

if A < B and B < C:
    print('Yes')
else:
    print('No')

# print('-----output-----')