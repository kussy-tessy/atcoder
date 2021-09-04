#!/usr/bin/env python3

S1 = input()
S2 = input()
S3 = input()

alls = set(['ABC', 'ARC', 'AGC', 'AHC'])
sets = set([S1, S2, S3])

print(list(alls-sets)[0])