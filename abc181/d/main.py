#!/usr/bin/env python3
from itertools import permutations
import sys
from random import randint
from collections import Counter

# 要は並び替えて下3桁が8で割り切れるのが作れたら嬉しい。
S = input()

# S = str(randint(1, 10000000))
# print(S)

eights = [str(8 * i).zfill(3) for i in range(125)]
# print(eights)

if len(S) <= 4: # よくわかんねーし4桁以下のときは総あたりでいいや
    ps = permutations(S, len(S))
    for p in ps:
        if int(''.join(p)) % 8 == 0:
            print('Yes')
            sys.exit()
    print('No')
else:
    c = Counter(S)
    for eight in eights:
        e = Counter(eight)
        is_ok = True
        for e_k, e_v in e.items():
            if e_v > c[e_k]:
                is_ok = False
        if is_ok:
            print('Yes')
            sys.exit()
    print('No')
    # for eight in eights:
    #     eight_l = list(eight)
    #     for S_ in S:
    #         if S_ in eight_l:
    #             eight_l.remove(S_)
    #     if len(eight_l) == 0:
    #         print('Yes')
    #         sys.exit()
    # print('No')