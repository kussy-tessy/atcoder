"""
具体的な色は分からないが、"色の多い順"にその人数を各iについて管理することは可能
"""

N = input()
As = list(map(int,(input().split())))

clr_cnts = [0, 0, 0]
ans = 1 # R, G, Bいずれもありうる

for A in As:
    if A in clr_cnts:
        i = clr_cnts.index(A)
    else:
        print(0)
        exit()
    clr_cnts_cnt = clr_cnts.count(A)
    clr_cnts[i] += 1
    # print(clr_cnts_cnt, clr_cnts)
    ans *= clr_cnts_cnt
    ans %= 1000000007

print(ans)