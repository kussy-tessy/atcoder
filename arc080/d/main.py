#!/usr/bin/env python3

H, W = map(int,(input().split()))
N = input()
As = list(map(int,(input().split())))

cells = [0] * (H*W)

s = 0
for c, A in enumerate(As):
    e = s + A
    for i in range(s, e):
        cells[i] = c + 1
    s = e

# Pythonで配列(list)をchunkに分割する
# https://gist.github.com/Himenon/c6c7b1a6a4543425eceda129107baa2a
def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

for t, chunk in enumerate(chunks(cells, W)):
    if t % 2 == 0:
        print(' '.join([str(c) for c in chunk]))
    else:
        print(' '.join([str(c) for c in chunk[::-1]]))

# print(cells)

