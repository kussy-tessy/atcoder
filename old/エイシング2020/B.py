# print('input >>')
N = input()
a_s = list(map(int,(input().split())))

ans = 0
for i, a in enumerate(a_s):
    if i % 2 == 0 and a % 2 == 1:
        ans += 1

# print('-----output-----')
print(ans)