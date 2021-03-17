def f(n):
    ans = 0
    while n > 0:
        n %= popcount(n)
        ans += 1
    return ans

def popcount(n):
    ans = 0
    while n > 0:
        ans += n % 2
        n //= 2 
    return ans

print('input >>')
N = int(input())
N = 10**5

X = input()
X = '1' * 10**5

X10 = int(X, 2)

x = []
for i in range(100):
    print(bin(i),f(i))


"""
for i, _ in enumerate(X):
    if X[i] == '0':
        X10anti = X10 + 2**(N-i-1)
    if X[i] == '1':
        X10anti = X10 - 2**(N-i-1)
    # print(popcount(X10anti))
    # print('hoge')

print('-----output-----')
"""