# print('input >>')
N = int(input())
mx = [[0] * 9 for i in range(9)]

for i in range(1, N+1):
    stri = str(i)
    if not stri[-1] == '0':    
        mx[int(stri[0])-1][int(stri[-1])-1] += 1


ans = 0
for j in range(1, N+1):
    strj = str(j)
    # print(strj[-1],"で始まり",strj[0],"で終わる",mx[int(strj[-1])-1][int(strj[0])-1])
    if not strj[-1] == '0':
        ans += mx[int(strj[-1])-1][int(strj[0])-1]

# print('-----output-----')
print(ans)