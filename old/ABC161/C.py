# print('input >>')
N, K = map(int,(input().split()))

mod = N % K

# print('-----output-----')
print(min(abs(mod-K), mod))