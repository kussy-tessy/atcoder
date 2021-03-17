# print('input >>')
N, K = map(int,(input().split()))
As = list(map(int,(input().split())))

for i in range(K, N):
    # next_prod = prod // As[i-K] * As[i]
    if As[i-K] < As[i]:
        print('Yes')
    else:
        print('No')
    # next_prod = prod

# print('-----output-----')