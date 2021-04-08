#!/usr/bin/env python3
from scipy.special import perm
# from math import factorial

N, K = map(int,input().split())
# print(perm(K, min(N, K),exact=True) * max(1, (K-1)**(N-1)))
print(K * max(1, (K-1)**(N-1)))