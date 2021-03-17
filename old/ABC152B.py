# print('input >>')
a, b = map(int,(input().split()))

# print('-----output-----')
if a > b:
    print(str(b) * a)
else:
    print(str(a) * b)