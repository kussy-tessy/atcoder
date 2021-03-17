# print('input >>')
N = int(input())
MOD = 10 ** 9 + 7

# print('-----output-----')
print((10 ** N - (2 * (9 ** N) - 8 ** N)) % MOD)