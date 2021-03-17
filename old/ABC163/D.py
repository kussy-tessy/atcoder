# print('input >>')
N, K = map(int,(input().split()))

MOD = 10**9+7

# print('-----output-----')
ans = 0
for n in range(K, N+2):
    max_ = n * (N-n+1 + N) // 2
    min_ = n * (0 + n-1) // 2
    # print(n, max_, min_)
    ans += max_ - (min_ -1)

print(ans % MOD)