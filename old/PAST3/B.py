import numpy as np

# print('input >>')
N, M, Q = map(int,(input().split()))
score = np.array([0] + [N] * M)
solved = np.array([[0] * (M+1) for _ in range(N+1)])

ans = []

for _ in range(Q):
    query = list(map(int,(input().split())))
    if query[0] == 1:
        answerer = query[1]
        ans.append(sum(score * solved[answerer]))
    else:
        answerer = query[1]
        prob = query[2]
        score[prob] -= 1
        solved[answerer][prob] += 1

# print('-----output-----')

for ans_ in ans:
    print(ans_)