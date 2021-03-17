# print('input >>')
N = int(input())
A = list(map(lambda A_e:int(A_e)-1, (input().split())))

for i in range(N):
    j = 0
    next_ = i
    while True:
        next_ = A.index(next_)
        j += 1
        if i == next_:
            print(j, end=' ')
            break

# print('-----output-----')