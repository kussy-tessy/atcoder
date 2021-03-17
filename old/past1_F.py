import re

# print('input >>')
S = input()

pattern = '[A-Z].*?[A-Z]'
matches = re.findall(pattern, S)

ls = []
for match in matches:
    ls.append((match, match.upper()))
ls.sort(key=lambda x:x[1])

# print('-----output-----')
for l in ls:
    print(l[0], end='')