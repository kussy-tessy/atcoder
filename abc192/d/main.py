#!/usr/bin/env python3

# https://iatlex.com/python/base_change#10n-2
def Base_n_to_10(X,n):
    out = 0
    for i in range(1,len(str(X))+1):
        out += int(X[-i])*(n**(i-1))
    return out#int out

X = input() # str
M = int(input())

X_max_digit = int(max(list(str(X))))

# https://twitter.com/meguru_comp/status/697008509376835584/photo/3
# ok = X_max_digit # ??
ok = X_max_digit # ??
ng = 10 ** 100

if len(X) == 1:
    if int(X) <= M:
        print(1)
    else:
        print(0)
    exit()

while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if int(Base_n_to_10(X, mid)) <= M:
        ok = mid
    else:
        ng = mid

print(ok - X_max_digit)