# print('input >>')
N = int(input())
a = list(map(int,(input().split())))

breaks = 0
count = 1
for i in range(N):
    if a[i] == count:
        count += 1
    else:
        breaks += 1

# print('-----output-----')
if breaks == N:
    print(-1)
else:
    print(breaks)