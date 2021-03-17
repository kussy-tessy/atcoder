# print('input >>')
N, Q = map(int,(input().split()))
follows = [[0] * N for _ in range(N)]
logs = []

for _ in range(Q):
    logs.append(input())

for log in logs: 
    log_info = log.split()
    person = int(log_info[1])-1
    
    if log_info[0] == '1':
        follows[person][int(log_info[2])-1] = 1
    elif log_info[0] == '2':
        for i in range(N):
            if follows[i][person] == 1:
                follows[person][i] = 1
    elif log_info[0] == '3':
        xs = []
        for i in range(N):
            if follows[person][i] == 1:
                xs.append(i)
        for x in xs:
            for j in range(N):
                if follows[x][j] == 1:
                    follows[person][j] = 1

# print('-----output-----')
for i, fs in enumerate(follows):
    for j, f in enumerate(fs):
        if f == 1 and i != j:
            print('Y', end='')
        else:
            print('N', end='')
    print()