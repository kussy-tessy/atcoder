# print('input >>')
N, M = map(int,(input().split()))
As = list(map(int,(input().split())))

days = sum(As)
free_days = N - days

# print('-----output-----')
if free_days >= 0:
    print(free_days)
else:
    print(-1)