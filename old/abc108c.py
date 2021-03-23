from collections import Counter

# print('input >>')
N, K = map(int, (input().split()))

A = [0] * N
for i in range(N):
    A[i] = (i + 1) % K

Acount = Counter(A)
# print('ACount %s' % Acount)
ans = 0
for mod, times in Acount.items():
    mod_anti = K - mod
    if (K - mod) * 2 % K == 0:
        ans += Acount[mod] ** 3

# print('----------output----------')
print(ans)