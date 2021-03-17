# print('input >>')
N = input()
N = reversed(N)
ans = 0
nxt = False
for n in N:
    i_n = int(n) + nxt
    if i_n % 10 >= 6:
        ans += 10 - i_n % 10
        nxt = True
    else:
        ans += i_n % 10
        nxt = False
    # print(N, ans)

# print('-----output-----')
print(ans)