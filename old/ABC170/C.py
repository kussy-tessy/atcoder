# print('input >>')
X, N = map(int,(input().split()))
ps = list(map(int,(input().split())))

all_num = [i for i in range(0, 102)]

for p in ps: # 10000
    all_num.remove(p)

diff = 1000
ans = 1000
anss = []

for num in all_num:
    my_diff = abs(num - X)
    if my_diff < diff:
        ans = num
        diff = my_diff

# print('-----output-----')
print(ans)