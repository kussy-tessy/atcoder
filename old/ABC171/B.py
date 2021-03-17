# print('input >>')
N, K = map(int,(input().split()))
ps = list(map(int,(input().split())))
ps.sort()

# print('-----output-----')
print(sum(ps[:K]))