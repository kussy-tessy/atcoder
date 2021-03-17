# print('input >>')
N, X, Y = map(int,(input().split()))
ans = [0] * N

for i in range(1, N+1):
    for j in range(i, N+1):
        choku = j-i
        tanraku = abs(X-i) + abs(Y-j) + 1
        ans[min(choku, tanraku)] += 1

# print('-----output-----')
for ans_e in ans[1:]:
    print(ans_e)