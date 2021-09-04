#!/usr/bin/env python3

A, B, C = map(int,(input().split()))

print(max(A+B, B+C, C+A))