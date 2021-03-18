# print('input >>')
N = int(input())

rest = N
i = 0
ans_l = []

while not rest == 0:
    if rest % (-2)**(i+1) == 0:
        ans_l.append('0')
    else:
        ans_l.append('1')
        rest -= (-2)**i
    i += 1

# print('----------output----------')
ans = ''.join(ans_l[::-1])
if N == 0:
    ans = 0

print(ans)