# print('input >>')
H, N = map(int,(input().split()))
A = list(map(int,(input().split())))

ans = 'Yes' if sum(A) >= H else 'No'
# print('-----output-----')
print(ans)