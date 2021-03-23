import numpy as np

# print('input >>')
N, K = map(int, (input().split()))
h = []
for _ in range(N):
    h.append(int(input()))

h.sort()
hdiff = [h[i + 1] - h[i] for i in range(len(h) - 1)]
hdiff = np.array(hdiff)
ans = np.sum(hdiff[0:0+K-1])
# print('hdiff: %s' % hdiff)
sum_ = np.sum(hdiff[0:0+K-1])
for i in range(1, N-K+1):
    # print('i %s' % i)
    # print('hdiff[i:i+K-1]: %s' % hdiff[i:i+K-1])]
    sum_ = sum_-hdiff[i-1]+hdiff[i+K-2]
    ans = min(ans, sum_)

# print('----------output----------')
print(ans)