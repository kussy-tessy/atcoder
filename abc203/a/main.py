#!/usr/bin/env python3

a, b, c = map(int,(input().split()))

se = set([a, b, c])

if len(se) == 3:
    print(0)
elif len(se) == 2:
    if a == b:
        print(c)
    elif b == c:
        print(a)
    elif c == a:
        print(b)
else:
    print(list(se)[0])