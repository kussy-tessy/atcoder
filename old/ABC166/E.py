# print('input >>')
N = int(input())
As = list(map(int,(input().split())))

tashi = {}
hiki = {}

for i in range(len(As)):
    sum_ = i + As[i]
    sub_ = i - As[i]
    if not sum_ in tashi:
        tashi[sum_] = 0
    if not sub_ in hiki:
        hiki[sub_] = 0
    tashi[sum_] += 1
    hiki[sub_] += 1

ans = 0

for k, v in tashi.items():
    if k in hiki:
        ans += v * hiki[k]

# print('-----output-----')
print(ans)