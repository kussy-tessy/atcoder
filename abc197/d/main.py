#!/usr/bin/env python3
from math import pi, sin, cos

N = int(input())
x0, y0 = map(int, input().split())
x_oppo, y_oppo = map(int, input().split())
x_center, y_center = (x0+x_oppo) / 2, (y0+y_oppo) / 2

theta = 2*pi / N
x0 -= x_center
y0 -= y_center

x1 = x0*cos(theta) - y0*sin(theta)
y1 = x0*sin(theta) + y0*cos(theta)

x1 += x_center
y1 += y_center

print(x1, y1)