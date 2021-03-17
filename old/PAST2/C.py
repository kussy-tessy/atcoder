# print('input >>')
N = int(input())
S = []
for _ in range(N):
    S.append(input())

for i in reversed(range(N-1)):
    for j in range(2*N-2):
        # print(i,j)
        # print(S[i][j] == '#', S[i+1][j-1] == 'X', S[i+1][j] == 'X', S[i+1][j+1] == 'X')
        if S[i][j] == '#' and (S[i+1][j-1] == 'X' or S[i+1][j] == 'X' or S[i+1][j+1] == 'X'):
            S[i] = S[i][:j] + 'X' + S[i][j+1:]

# print('-----output-----')
print('\n'.join(S))