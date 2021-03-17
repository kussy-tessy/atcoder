# print('input >>')
N, K = map(int,(input().split()))
H = list(map(int,(input().split())))

H.sort(reverse=True)

# print('-----output-----')
print(sum(H[K:]))