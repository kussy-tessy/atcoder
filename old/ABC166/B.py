# print('input >>')
N, K = map(int,(input().split()))
As = []
okashi = [0] * N

for _ in range(K):
    d = input()
    As.append(list(map(int,(input().split()))))

for A in As:
    for a in A:
        okashi[a-1] += 1

ans = 0
for okashi_ in okashi:
    if okashi_ == 0:
        ans += 1

# print('-----output-----')
print(ans)