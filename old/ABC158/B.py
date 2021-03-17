# print('input >>')
N, A, B = map(int,(input().split()))

# print('-----output-----')
print(N // (A+B) * A + min(N % (A+B), A))