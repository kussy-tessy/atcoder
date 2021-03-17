# print('input >>')
N = int(input())
Xs = list(map(int,(input().split())))

ans = 10 ** 10
for i in range(1,101):
    mps = 0
    for X in Xs:
        mps += (X - i)**2
    ans = min(ans, mps)

# print('-----output-----')
print(ans)