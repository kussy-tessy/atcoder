# print('input >>')

N, K = map(int,(input().split()))
r, s, p = map(int,(input().split()))
T = input()

point = 0

my = []

for i in range(K):
    if T[i] == 'r': # グーなら
        point += p # パー出す
        my.append('p')
    elif T[i] == 's': # チョキなら
        point += r # グー出す
        my.append('r')
    elif T[i] == 'p': # パーなら
        point += s # チョキだす
        my.append('s')

# 縛り以降
for i in range(K, len(T)):
    if T[i] == 'r': # グーなら
        if not my[i-K] == 'p': # パーが出せるなら
            point += p
            my.append('p')
        else:
            my.append('r')
    if T[i] == 's': # チョキなら
        if not my[i-K] == 'r': # グーが出せるなら
            point += r
            my.append('r')
        else:
            my.append('s')
    if T[i] == 'p': # パーなら
        if not my[i-K] == 's': # チョキが出せるなら
            point += s
            my.append('s')
        else:
            my.append('p')


# print('-----output-----')
print(point)