#!/usr/bin/env python3

import decimal

a, b, x = map(int,(input().split()))

print(b // x - (a-1) // x)