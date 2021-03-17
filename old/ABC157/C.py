import sys

def is_ok(i, conds):
    str_i = str(i)
    for cond in conds:
        if len(str_i) <= cond[0]-1:
            return False
        if not str_i[cond[0]-1] == str(cond[1]):
            return False
    return True

# print('input >>')
N, M = map(int,(input().split()))
scs = []
for _ in range(M):
    scs.append(tuple(map(int,(input().split()))))

start = 10**(N-1) if N >=2 else 0

for i in range(start, 10**N):
    if is_ok(i, scs):
       print(i)
       sys.exit() 

print(-1)

# print('-----output-----')