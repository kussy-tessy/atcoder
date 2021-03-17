from collections import Counter

# print('input >>')
N = int(input())
Ss = [input() for _ in range(N)]

SsC = Counter(Ss)

print(len(SsC))

# print('-----output-----')