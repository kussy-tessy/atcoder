# print('input >>')
N = int(input())
P = list(map(int,(input().split())))

ans = 0
now = P[0]

for p in P:
    if now >= p:
        ans += 1
        now = p

# print('-----output-----')
print(ans)