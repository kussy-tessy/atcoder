from collections import Counter

# print('input >>')
N = int(input())
As = list(map(int,(input().split())))

c = Counter(As)

# print('-----output-----')
for i in range(1, N+1):
    print(c[i])