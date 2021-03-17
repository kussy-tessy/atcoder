import sys

# print('input >>')
X, Y = map(int,(input().split()))

for t in range(X+1):
    k = X - t
    if t * 2 + k * 4 == Y:
        print('Yes')
        sys.exit()

print('No')
# print('-----output-----')
