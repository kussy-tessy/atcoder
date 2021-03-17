from collections import deque

# print('input >>')
S = deque(input())
Q = int(input())
queries = []
for _ in range(Q):
    queries.append(input())

is_reverse = False

for q in queries:
    ql = list(q.split())
    if len(ql) == 1:
        is_reverse = not is_reverse
    else:
        if ql[1] == '1': # 先頭に加える
            if not is_reverse:
                S.appendleft(ql[2])
            else:
                S.append(ql[2])
        else: # 末尾に加える
            if not is_reverse:
                S.append(ql[2])
            else:
                S.appendleft(ql[2])

# print('-----output-----')
if not is_reverse:
    print(''.join(list(S)))
else:
    print(''.join(list(S)[::-1]))