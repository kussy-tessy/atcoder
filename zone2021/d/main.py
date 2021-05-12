#!/usr/bin/env python3

from collections import deque

S = input()

# R = ''
R = deque()
reverse = False

for s in S:
    if s == 'R':
        reverse = not reverse
    else:
        if reverse:
            # R = s + R
            R.appendleft(s)
        else:
            # R += s
            R.append(s)
    # print(R, reverse)

# R2 = ''
R2 = deque()

for r in R:
    if len(R2) == 0:
        R2.append(r)
    elif R2[-1] != r:
        R2.append(r)
    else:
        # R2 = R2[:-1]
        R2.pop()
    # print(R2)

if reverse:
    print(''.join(list(R2)[::-1]))
else:
    print(''.join(list(R2)))