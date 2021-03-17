#!/usr/bin/env python3

A, B, C = map(int,(input().split()))

if C == 0:
    if A == B:
        print('Aoki')
if C == 1:
    if A == B:
        print('Takahashi')

if A > B:
    print('Takahashi')
if A < B:
    print('Aoki')