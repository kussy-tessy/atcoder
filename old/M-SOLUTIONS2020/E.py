import numpy as np

def distance(Xline, Yline, XYPs):
    minDs = []
    for XYP in XYPs:
        X, Y, P = XYP[0], XYP[1], XYP[2]
        minX = minY = 10 ** 10
        for Xline_ in Xline:
            minX = min(minX, X-Xline_)
        for Yline_ in Yline:
            minY = min(minY, Y-Yline_)
        minD = min(minX*P, minY*P)
        minDs.append(minD)
    return min(minDs)

# print('input >>')
N = int(input())
XYPs = []

for _ in range(N):
    XYP = tuple(map(int,(input().split())))
    XYPs.append(XYP)

XYPs.sort(key=lambda XYP:XYP[2], reverse=True)

Xlines = [0]
Ylines = [0]

for XYP in XYPs:
    X = XYP[0]
    Y = XYP[1]
    print(distance(Xlines, Ylines, XYPs))
    if(distance(Xlines + [X], Ylines, XYPs) < distance(Xlines, Ylines + [Y], XYPs)):
        Xlines += [X]
    else:
        Ylines += [Y]

# print('-----output-----')