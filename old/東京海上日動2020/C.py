from random import randint

# print('input >>')
# N, K = map(int,(input().split()))
# As = list(map(int,(input().split())))

N, K = 30, 100
As = [0] * 30
As[0] = 1

# まずはナイーブにやる(TLEでもういいよ。。。)
for t in range(K):
    baseAs = [1] * len(As)
    for i in range(len(As)):
        d = As[i]
        if d == 1000:
            continue
        for j in range(d):
            if i-j-1 >= 0:
                baseAs[i-j-1] += 1
            if i+j+1 < len(As):
                baseAs[i+j+1] += 1
    As = baseAs[:]
    if all([A == N for A in As]):
        break
    print(As)

# print('-----output-----')
for A in As:
    print(A, end=' ')