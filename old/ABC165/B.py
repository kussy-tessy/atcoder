import math

# print('input >>')
X = int(input())
money = 100
i = 0
while True:
    i += 1
    money = math.floor(1.01*money)
    if money >= X:
        print(i)
        break

# print('-----output-----')