#!/usr/bin/env python3

N = int(input())

st = ''

def calc(n):
    global st
    # print(n)
    if n == 0:
        return
    if n % 2 == 0:
        st = 'B' + st
        return calc(n // 2)
    else:
        st = 'A' + st
        return calc(n - 1)

calc(N)

print(st)