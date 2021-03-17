#!/usr/bin/env python3

N = int(input())
xys = []

for _ in range(N):
    xys.append(tuple(map(int,(input().split()))))

# (xi, yi), (xj, yj)のマンハッタン距離は、
# max(|(xi+yi) - (xj+yj)|, |(xi-yi) - (xj-yj)|)となる
# つまりある1点のx,y座標同士の和同士の差の絶対値か
# x,y座標同士を引いたもの同士の差の絶対値のうち、大きい方がそれになる
# （引いたものに関しては符号が逆転してしまうが絶対値をつけるので問題ない）
# （式変形よりは図を見たほうがいいかも）
# よって(xi+yi)のできるだけ大きいものとできるだけ小さいもの
# (xi-yi)のできるだけ大きいものとできるだけ小さいものを探せば良い。

wa = [xy[0] + xy[1] for xy in xys]
sa = [xy[0] - xy[1] for xy in xys]

wa.sort()
sa.sort()

# print(wa)
# print(sa)

print(max(wa[-1] - wa[0], sa[-1] - sa[0]))
