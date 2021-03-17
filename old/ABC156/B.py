# print('input >>')
N, K = map(int,(input().split()))

n = 0
while True:
    if K ** n <= N:
        n+=1
    else:
        break
# print('-----output-----')
print(n)