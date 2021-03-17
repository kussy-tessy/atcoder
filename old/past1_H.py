# print('input >>')
N = int(input())
zaiko = list(map(int,(input().split())))
Q = int(input())
zentai_min = min(zaiko)
kisu_min = min(zaiko[0::2])
kisu = 0
zen = 0
ans = 0
kisu_num = N // 2
if N % 2 == 1:
    kisu_num += 1

for _ in range(Q):
    query = list(map(int,(input().split())))
    if query[0] == 1:
        query[1] -= 1
        if query[1] % 2 == 1: # 偶数
            if zaiko[query[1]] - zen >= query[2]:
                zaiko[query[1]] -= query[2]
                ans += query[2]
                zentai_min = min(zentai_min, zaiko[query[1]] - zen)
        else: # 奇数
            if zaiko[query[1]] - zen - kisu >= query[2]:
                zaiko[query[1]] -= query[2]
                ans += query[2]
                kisu_min = min(kisu_min, zaiko[query[1]] - zen - kisu)
                zentai_min = min(zentai_min, kisu_min)
    elif query[0] == 2:
        if kisu_min >= query[1]:
            ans += query[1] * kisu_num
            kisu += query[1]
            kisu_min -= query[1]
            zentai_min = min(zentai_min, kisu_min)
    elif query[0] == 3:
        if zentai_min >= query[1]:
            ans += query[1] * N
            zen += query[1]
            zentai_min -= query[1]
    # print(zaiko, zen, kisu, ans)

# print('-----output-----')
print(ans)