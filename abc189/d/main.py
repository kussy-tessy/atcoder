#!/usr/bin/env python3

N = int(input())
Ss = []
for _ in range(N):
    Ss.append(input())

if Ss[0] == 'AND':
    ans = 1 # [True, True]の1通り
else:
    ans = 3 # [True, False], [True, True], [False, True]の3通り

for i, S in enumerate(Ss[1:]):
    # SがANDであるときは、その部分は[True, True]とせざるを得ずパターンは増えない
    if S == 'AND': 
        ans = ans
    # SがORであるときは、その部分は[True, False], [True, True]の2パターンに加え、
    # [False, True]がある。後者は今までの全パータンの余事象に相当するので、2^nからansを減ずる
    else:
        ans = 2 * ans + (2**(i+2) - ans)

print(ans)