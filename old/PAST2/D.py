import sys

# print('input >>')
S = input()

patterns = set()

patterns.add('.')

# １文字
for i in range(len(S)):
    st = S[i]
    patterns.add(st)

if len(S) == 1:
    print(len(patterns))
    sys.exit()

# 2文字
patterns.add('..')

for i in range(len(S)-1):
    st1 = S[i] + S[i+1]
    st2 = '.' + S[i+1]
    st3 = S[i] + '.'
    patterns.add(st1)
    patterns.add(st2)
    patterns.add(st3)

if len(S) == 2:
    print(len(patterns))
    sys.exit()

patterns.add('...')

# 3文字
for i in range(len(S)-2):
    st1 = S[i] + S[i+1] + S[i+2]
    st2 = '.' + S[i+1] + S[i+2]
    st3 = S[i] + '.' + S[i+2]
    st4 = S[i] + S[i+1] + '.'
    st5 = S[i] + '.' + '.'
    st6 = '.' + S[i+1] + '.'
    st7 = '.' + '.' + S[i+2]
    patterns.add(st1)
    patterns.add(st2)
    patterns.add(st3)
    patterns.add(st4)
    patterns.add(st5)
    patterns.add(st6)
    patterns.add(st7)

# print('-----output-----')
print(len(patterns))