#!/usr/bin/env python3

s = input()
K = int(input())

def to_ord(char):
    return ord(char) - 97
def next_char(char, times):
    return chr((to_ord(char) + times) % 26 + 97)

for i, s_ in enumerate(s):
    if i == len(s)-1:
        print(next_char(s_, K))
    elif s_ == 'a':
        print('a', end='')
    elif K >= 26 - to_ord(s_):
        print(next_char(s_, 26-to_ord(s_)), end='')
        K -= 26-to_ord(s_)
    else:
        print(s_, end='')