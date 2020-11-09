# print('input >>')
N, K = map(int, (input().split()))
x = list(map(int, (input().split())))

neg = 0
pos = 0

left = 0
right = 0

ans = 10**10

for l in range(N - K + 1):
    left = x[l]
    right = x[l + K - 1]
    neg = min(left, 0)
    pos = max(right, 0)
    if neg < 0 and pos > 0:
        ans = min(ans, abs(neg) * 2 + pos, abs(neg) + pos * 2)
    else:
        ans = min(ans, abs(neg) + pos)

# print('----------output----------')
print(ans)