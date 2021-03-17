#!/usr/bin/env python3

N, X = map(int,(input().split()))
As = list(map(int,(input().split())))

ans = [str(A) for A in As if A != X]
# print(ans)
print(' '.join(ans))
