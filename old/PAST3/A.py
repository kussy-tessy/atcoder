# print('input >>')
s = input()
t = input()

# print('-----output-----')

if s == t:
    print('same')
elif s.lower() == t.lower():
    print('case-insensitive')
else:
    print('different')