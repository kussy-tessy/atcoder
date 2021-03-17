#!/usr/bin/env python3

B, C = map(int,(input().split()))

if B > 0:
    if C == 1:
        print(2)
    elif C == 2:
        print(3)
    elif C <= 2 * B:
        print(3 + 2 * (C - 2))
    else:
        print(3 + 2 * (2*B - 2) + (C - 2*B))
elif B == 0:
    if C == 1:
        print(1)
    elif C >= 2:
        print(1 + (C-1))
elif B < 0:
    if C == 1:
        print(2)
    elif C == 2:
        print(3)
    elif C <= 2 * B + 1:# testcase
        print(3 + 2 * (C - 2))
    else:
        print(3 + 2 * (2*abs(B) + 1 - 2) + (C - (2*abs(B)+1)))