#!/usr/bin/env python3
from math import ceil

N = int(input())
T = input()

# まず含まないかどうかを調べる
if not T in '110' * (2*(10**5) // 3 + 5):
    print(0)
# そうでないとき
else:
    # 1のみでTが構成されているとき
    if T == '1':
        print(2 * 10**10)
    elif T == '11':
        print(10**10)
    # そうでないときは必ず0を含む。0の数を数えておく
    else:
        zeros = sum([1 if t == '0' else 0 for t in T])
        # 末尾が1のとき
        if T[-1] == '1':
            print(10**10 - zeros)
        # 末尾が0のとき
        elif T[-1] == '0':
            print(10**10 - zeros + 1)

"""
if T == '0':
    print(10**10)
elif T == '1':
    print((10**10)*2)
elif T == '10':
    print(10**10)
elif T == '11':
    print(10**10)
elif T == '00':
    print(0)
elif T == '01':
    print(10**10-1)
else:
    rep = ceil((N+1) / 3)
    s = '110' * rep
    cnt = 0
    for i in range(len(s)-N):
        if s[i:1+N] == T:
            cnt += 1
    if cnt == 0:
        print(0)
    elif cnt == 1:
        print(10**10 - rep + 1)
    elif cnt == 2:
        print(10**10 - rep + 2)
"""