#!/usr/bin/env python3

A, B, C = map(int,(input().split()))

if C % 2 == 0:
    C = 2
else:
    C = 1

if A ** C > B ** C:
    print(">")
elif A ** C < B ** C:
    print("<")
else:
    print("=")
