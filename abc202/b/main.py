#!/usr/bin/env python3

S = input()

# conv_dict = {'0': '0', '1': '1', '6': '9', }

for s in reversed(S):
    if s == '6':
        print('9', end='')
    elif s == '9':
        print('6', end='')
    else:
        print(s, end='')
print()