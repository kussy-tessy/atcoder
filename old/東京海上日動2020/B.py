# print('input >>')
A, V = map(int,(input().split()))
B, W = map(int,(input().split()))
T = int(input())


if W >= V:
    print('NO')
elif abs(B-A) / (V-W) <= T:
    print('YES')
else:
    print('NO')

# print('-----output-----')