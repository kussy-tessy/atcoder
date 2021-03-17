from math import sqrt

def is_prime(x):
    for i in range(2, int(sqrt(x))):
        if x % i == 0:
            return False
    return True

# print('input >>')
X = int(input())

while True:
    if is_prime(X):
        print(X)
        exit()
    X += 1

# print('-----output-----')