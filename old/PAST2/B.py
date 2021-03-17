from collections import Counter

# print('input >>')
S = input()

# print('-----output-----')
counter = Counter(S)
c_common = counter.most_common()

print(c_common[0][0])