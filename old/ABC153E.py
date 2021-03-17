# print('input >>')
H, N = map(int,(input().split()))
ABs = []
for _ in range(N):
    ABs.append(tuple(map(int,(input().split()))))

ABs.sort(key=lambda x: x[1])
ABs.sort(key=lambda x: x[0]/x[1], reverse=True)
ans = 0

# print(ABs)
for AB in ABs:
    # print(AB[0] / AB[1])
    if AB[0] <= H:
        times = H // AB[0]
    else:
        times = 1
    H -= AB[0] * times
    ans += AB[1] * times
    # print('times', times, 'H', H, 'damage', AB[1] * times, 'ans', ans)
    if H <= 0:
        break

# print('-----output-----')
print(ans)