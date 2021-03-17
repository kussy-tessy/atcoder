#!/usr/bin/env python3

import re

s = input()

l = 0

# s = 'S10H10SAS2D2C3H5H4CA'

cards = []

# もしかして間違っていたのってこのロジック……？
for r in range(1, len(s)):
    if s[r] in ['S' ,'H', 'D', 'C']:
        cards.append(s[l:r])
        l = r
cards.append(s[l:])

# print(cards)

# s = s.replace('10', 'T')
# for i in range(0, len(s), 2):
#     cards.append(s[i:i+2])

# print(cards)
# for i in range(len(cards)):
#     cards[i] = cards[i].replace('T', '10')

suits = ['S', 'H', 'D', 'C'] 
nums = ['10', 'J', 'Q', 'K', 'A']

ss = 0
hs = 0
ds = 0
cs = 0

i = 0

# mark = 'H' # わからんでばっぐ
for card in cards:
    for suit in suits:
        for num in nums:
            if card == suit + num:
                if suit == 'S':
                    ss += 1
                elif suit == 'H':
                    hs += 1
                elif suit == 'D':
                    ds += 1
                elif suit == 'C':
                    cs += 1
    if ss >= 5:
        mark = 'S'
        break
    if hs >= 5:
        mark = 'H'
        break
    if ds >= 5:
        mark = 'D'
        break
    if cs >= 5:
        mark = 'C'
        break
    i += 1

ans = ''

# えーーーーーなんでええええええええmarkが決まらないパターンとかあるのおおお
# 保証されてるんでしょう？？？？

for suit in suits:
    if mark == suit:
        for card in cards[:i]:
            if not (card[0] == suit and card[1:] in nums):
                ans += card

if ans == '':
    print(0)
else:
    print(ans)

"""
s_rsf = [None] * 5
h_rsf = [None] * 5
d_rsf = [None] * 5
c_rsf = [None] * 5

a = []
df = None
for i in range(len(cards)):
    s = cards[i]
    a.append(i)
    if s == 'S10':
        s_rsf[0] = i
    elif s == 'SJ':
        s_rsf[1] = i
    elif s == 'SQ':
        s_rsf[2] = i
    elif s == 'SK':
        s_rsf[3] = i
    elif s == 'SA':
        s_rsf[4] = i

    elif s == 'H10':
        h_rsf[0] = i
    elif s == 'HJ':
        h_rsf[1] = i
    elif s == 'HQ':
        h_rsf[2] = i
    elif s == 'HK':
        h_rsf[3] = i
    elif s == 'HA':
        h_rsf[4] = i

    elif s == 'D10':
        d_rsf[0] = i
    elif s == 'DJ':
        d_rsf[1] = i
    elif s == 'DQ':
        d_rsf[2] = i
    elif s == 'DK':
        d_rsf[3] = i
    elif s == 'DA':
        d_rsf[4] = i

    elif s == 'C10':
        c_rsf[0] = i
    elif s == 'CJ':
        c_rsf[1] = i
    elif s == 'CQ':
        c_rsf[2] = i
    elif s == 'CK':
        c_rsf[3] = i
    elif s == 'CA':
        c_rsf[4] = i

    if all([not s is None for s in s_rsf]):
        df = set(a) - set(s_rsf)
    elif all([not s is None for s in h_rsf]):
        df = set(a) - set(h_rsf)
    elif all([not s is None for s in d_rsf]):
        df = set(a) - set(d_rsf)
    elif all([not s is None for s in c_rsf]):
        df = set(a) - set(c_rsf)

    if not df is None:
        # print(df)
        if len(df) == 0:
            print(0)
            break
        for df_ in sorted(list(df)):
            print(cards[df_], end='')
        print()
        break
"""