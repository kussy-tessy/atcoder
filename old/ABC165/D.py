import sys

def formula(A, B, x):
    return (A * x) // B - A * (x // B)

# print('input >>')
# print('-----output-----')

A, B, X = map(int,(input().split()))

bottom = 1
top = X

while True:
    if formula(A, B, bottom) <= formula(A, B, top):
        mid = bottom + top // X
        if formula(A, B, mid) > formula(A, B, top):
            bottom = mid
        else:
            