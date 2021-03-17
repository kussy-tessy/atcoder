# print('input >>')
A, B, M = map(int,(input().split()))
al = list(map(int,(input().split())))
bl = list(map(int,(input().split())))
xyms = []
for _ in range(M):
    xyms.append(list(map(int,(input().split()))))


ans = min(al) + min(bl)
for xym in xyms:
    x = xym[0]
    y = xym[1]
    m = xym[2]
    ans = min(al[x-1] + bl[y-1] - m, ans)

# print('-----output-----')
print(ans)