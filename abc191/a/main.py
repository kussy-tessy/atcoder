#!/usr/bin/env python3
import decimal

V, T, S, D = map(int,(input().split()))

"""
time = decimal.Decimal(str(D / V))

if T <= time <= D:
    print('No')
else:
    print('Yes')
"""

t_p = V * T
s_p = V * S

if t_p <= D <= s_p:
    print('No')
else:
    print('Yes')