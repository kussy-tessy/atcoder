# print('input >>')
N = input()

gokei = sum([int(n) for n in N])

# print('-----output-----')
if gokei % 9 == 0:
    print('Yes')
else:
    print('No')