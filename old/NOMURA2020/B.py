# print('input >>')
T = input()

ans = ''

"""
i = 0
while i < len(T)-1:
    # print(i)
    if T[i] == 'P':
        ans += 'P'
    elif T[i] == 'D':
        ans += 'D'
    elif T[i] == '?':
        if T[i:i+2] == '??':
            ans += 'PD'
            i += 1
        elif T[i:i+2] == '?P':
            ans += 'DP'
            i += 1
        elif T[i:i+2] == '?D':
            ans += 'PD'
            i += 1
    i += 1
    # print(ans)

# print(i)
if not i == len(T):
    if T[-1] == '?':
        ans += 'D'
    else:
        ans += T[-1]
"""

for t in T:
    if t == '?':
        ans += 'D'
    else:
        ans += t


# print('-----output-----')
print(ans)