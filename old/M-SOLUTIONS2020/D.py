# print('input >>')
N = input()
As = list(map(int,(input().split())))

money = 1000
kab = 0

for i in range(len(As)-1):
    if As[i+1] >= As[i]:
        kounyu = money // As[i]
        kab += kounyu
        money -= kounyu * As[i]
    elif As[i+1] < As[i]:
        money += kab * As[i]
        kab = 0
    # print(money, kab)

money += kab * As[-1]

# print('-----output-----')
print(money)