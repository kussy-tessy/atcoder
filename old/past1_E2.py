# print('input >>')
N, Q = map(int,(input().split()))
follows = [[] * N for _ in range(N)]
logs = []

for _ in range(Q):
    logs.append(input())

for log in logs: 
    log_info = log.split()
    person = int(log_info[1])-1
    
    if log_info[0] == '1':
        follows[person].append(int(log_info[1])-1)
    elif log_info[0] == '2':
        for i, p in enumerate(follows):
            for followee in p:
                if followee == person:
                    follows[person].append(i)
    elif log_info[0] == '3':
        for followee in follows[person]:
            follows[person] += follows[followee]

# print('-----output-----')
for fs in follows:
    ls = list(set(fs)).sort
    ar = [0] * N
    for l in ls:
        ar[l] = 1
    for a in ar:
        if a == 1:
            print('Y', end='')
        else:
            print('N', end='')
        print()