from collections import Counter

# print('input >>')
N = int(input())
c = input()

counter = Counter(c)
R_cnt = counter['R']
W_cnt = counter['W']

ans = 0
for s in c[:R_cnt]:
    if s == 'W':
        ans += 1

# print('-----output-----')
print(ans)