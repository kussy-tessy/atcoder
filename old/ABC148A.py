# print('input >>')
a = int(input())
b = int(input())

li = set([1,2,3])

ans = li - set([a,b])

# print('-----output-----')

print(list(ans)[0])