#!/usr/bin/env python3

from decimal import Decimal
A, B = input().split()

A = Decimal(A)
B = Decimal(B)

print((1-B/A) * 100)