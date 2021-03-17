import itertools

# print('input >>')
N = int(input())
Ls = list(map(int,(input().split())))
Ls.sort()

combs = itertools.combinations(Ls, 3)

ans = 0
for comb in combs:
    if (comb[0] != comb[1] and comb[1] != comb[2] and comb[2] != comb[0] 
      and comb[0] + comb[1] > comb[2]):
        ans += 1

# print('-----output-----')
print(ans)