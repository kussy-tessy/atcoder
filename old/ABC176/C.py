# print('input >>')
N = input()
As = list(map(int,(input().split())))

ans = 0
for i in range(len(As) - 1):
    if As[i] > As[i+1]:
        ans += As[i] - As[i+1]
        As[i+1] += As[i] - As[i+1]

# print('-----output-----')
print(ans)
# print(As)