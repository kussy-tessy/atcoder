# print('input >>')
N, R = map(int,(input().split()))

if N <= 10:
    ans = R + 100 * (10-N)
else:
    ans = R

# print('-----output-----')
print(ans)