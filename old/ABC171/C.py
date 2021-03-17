# print('input >>')
N = int(input())
alphabets = 'abcdefghijklmnopqrstuvwxyz'

name = ''

while N > 0:
    mod = N % 26
    if mod == 0:
        mod = int(26)
    name = alphabets[int(mod-1)] + name
    N -= 0.1
    N //= 26

# print('-----output-----')
print(name)