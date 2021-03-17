import sys

# print('input >>')
N, M = map(int,(input().split()))
As = list(map(int,(input().split())))

border = sum(As)*1/(4*M)
As_best = sorted(As, reverse=True)[:M]

for A in As_best:
    if A < border:
        print('No')
        sys.exit()
print('Yes')

# print('-----output-----')