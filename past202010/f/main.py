#!/usr/bin/env python3

from collections import Counter

# print('input >>')
N, K = map(int,(input().split()))
Ss = []
for _ in range(N):
    Ss.append(input())

commons = Counter(Ss).most_common()
(S, cnt) = commons[K-1]

# print('-----output-----')
if len([None for (S_, cnt_) in commons if cnt_ == cnt]) > 1:
    print('AMBIGUOUS')
else:
    print(S)
