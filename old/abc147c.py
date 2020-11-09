from itertools import product

# print('input >>')
N = int(input())
G = []
for i in range(N):
    A_i = int(input())
    edges = {}
    for n in range(A_i):
        edge = tuple(map(int, (input().split())))
        edges[edge[0]] = edge[1]
    G.append(edges)

prods = product([0,1], repeat=N)
ans = 0

for prod in prods:
    flg = True
    for i, h in enumerate(prod):
        if h == 1:  # 正直者ならその人の言うことを調べる
            shougens = G[i]
            for hito, docchi in shougens.items():
                if (docchi == 1 and prod[hito-1] == 0) or (docchi == 0 and prod[hito-1] == 1):
                    flg = False
    if flg:
        ans = max(ans, sum(prod)) # ここまで来れたら矛盾が生じなかった

# print('----------output----------')
print(ans)