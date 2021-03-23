# print('input >>')
N = input()
S = input()

ans = 1
left = S[0]
for s in S:
    if not s == left:
        ans += 1
        left = s

# print('----------output----------')
print(ans)