#!/usr/bin/env python3
MOD = 200

N = int(input())
As = list(map(int,(input().split())))

As_mod = [A % MOD for A in As]

m_dict = {}

for i, As_mod_ in enumerate(As_mod):
    if not As_mod_ in m_dict:
        m_dict[As_mod_] = []
    m_dict[As_mod_].append(i)

for v in m_dict.values():
    if len(v) > 1:
        print('Yes')
        print(1, v[0]+1)
        print(1, v[1]+1)
        exit()

# 以下だめだめ。記念提出
p = [-1] * MOD
p[0] = 0

members = m_dict.keys()
print(members)

for member in members:
    for i in range(len(p), 0):
        if p[i] != -1:
            p[(i+member) % MOD] = member
            # p[(i+member)] = member
