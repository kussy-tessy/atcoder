def itti(S, T):
    ans = 0
    for i in range(len(S)):
        if S[i] == T[i]:
            ans += 1
    return ans

# print('input >>')
S = input()
T = input()

ans = 0
for i in range(len(S)-len(T)+1):
    ans = max(ans, itti(S[i: i+len(T)], T))

# print('-----output-----')
print(len(T)-ans)