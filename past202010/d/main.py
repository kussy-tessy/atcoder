#!/usr/bin/env python3

from sys import exit

# print('input >>')
S = input()
Ls = input() + '#' # 最後にリストに強制的に追加するため

blanks = []
ren = False

for L in Ls:
    if L == '.':
        if not ren:
            ren = True
            blank = 1
        else:
            blank += 1
    else:
        if ren:
            ren = False
            blanks.append(blank)

# print(blanks)

if len(blanks) == 0:
    print(0, 0)
    exit()

if Ls[0] == '.':
    left = blanks[0]
else:
    left = 0

if Ls[-2] == '.':
    right = blanks[-1]
else:
    right = 0

blanks_max = max(blanks)
extra = max(0, blanks_max - (left + right))

# print('-----output-----')
print(left + extra, right)