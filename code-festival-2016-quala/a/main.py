#!/usr/bin/env python3

s = input()
K = int(input())

def to_ord(char):
    return ord(char) - 97
def next_char(char, times):
    return chr((to_ord(char) + times) % 26 + 97)

print(to_ord('a'))
print(to_ord('b'))
print(next_char('b', 5))
print(next_char('z', 1))