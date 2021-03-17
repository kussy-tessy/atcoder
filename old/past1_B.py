# print('input >>')
N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

for i in range(N-1):
    diff = A[i+1] - A[i]
    if diff == 0:
        print('stay')
    elif diff > 0:
        print('up', diff)
    else:
        print('down', abs(diff))

# print('-----output-----')