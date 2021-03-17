def calc(first, second, last_li, last):
    ans = 0
    for i in range(len(S)):
        if S[i] == first:
            for j in range(i+1, len(S)):
                if S[j] == second:
                    ans += (last_li+[0])[j+1]
                    if j+j-i < len(Bs) and S[j+j-i] == last:
                        ans -= 1
    return ans

# print('input >>')
N = int(input())
S = input()

Rs_add = [0] * len(S)
for i in reversed(range(len(Rs_add)-1)):
    if S[i] == 'R':
        Rs_add[i] = Rs_add[i+1] + 1
    else:
        Rs_add[i] = Rs_add[i+1]
Gs_add = [0] * len(S)
for i in reversed(range(len(Gs_add)-1)):
    if S[i] == 'G':
        Gs_add[i] = Gs_add[i+1] + 1
    else:
        Rs_add[i] = Rs_add[i+1]
Bs_add = [0] * len(S)
for i in reversed(range(len(Bs_add)-1)):
    if S[i] == 'B':
        Bs_add[i] = Bs_add[i+1] + 1
    else:
        Bs_add[i] = Bs_add[i+1]

"""
Rs = [1 if i == 'R' else 0 for i in S]
Gs = [1 if i == 'G' else 0 for i in S]
Bs = [1 if i == 'B' else 0 for i in S]

Rs_add = [0] * len(S)
Rs_add[0] = sum(Rs)
Gs_add = [0] * len(S)
Gs_add[0] = sum(Gs)
Bs_add = [0] * len(S)
Bs_add[0] = sum(Bs)

for i in range(len(Rs)-1):
    if Rs[i] == 1:
        Rs_add[i+1] = Rs_add[i]-1
    else:
        Rs_add[i+1] = Rs_add[i]
for i in range(len(Gs)-1):
    if Gs[i] == 1:
        Gs_add[i+1] = Gs_add[i]-1
    else:
        Gs_add[i+1] = Gs_add[i]
for i in range(len(Bs)-1):
    if Bs[i] == 1:
        Bs_add[i+1] = Bs_add[i]-1
    else:
        Bs_add[i+1] = Bs_add[i]
"""


ans = 0

ans += calc('R', 'G', Bs_add, 'B')
ans += calc('G', 'R', Bs_add, 'B')
ans += calc('R', 'B', Gs_add, 'G')
ans += calc('B', 'R', Gs_add, 'G')
ans += calc('G', 'B', Rs_add, 'R')
ans += calc('B', 'G', Rs_add, 'R')


# print('-----output-----')
print(ans)