# print('input >>')
S = input()
K = int(input())

s_left = '1'
num_1 = 0

for s in S:
    if s == '1':
        num_1 += 1
    else:
        s_left = s
        break

if K <= num_1:
    ans = '1'
else:
    ans = s_left

# print('----------output----------')
print(ans)