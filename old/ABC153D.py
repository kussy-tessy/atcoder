# print('input >>')
H = int(input())

ans = 0
cnt = 1
while True:
    H //= 2
    ans += cnt
    cnt *= 2
    if H == 0:
        break

# print('-----output-----')
print(ans)