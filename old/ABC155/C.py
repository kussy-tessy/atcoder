from collections import Counter

# print('input >>')

N = int(input())
Ss = []
for _ in range(N):
    Ss.append(input())

Ss_cnt = Counter(Ss)
common = Ss_cnt.most_common()
most = common[0][1]
cand = []
for e in common:
    if e[1] == most:
        cand.append(e[0])
    else:
        break

cand.sort()

# print('-----output-----')
for c in cand:
    print(c)