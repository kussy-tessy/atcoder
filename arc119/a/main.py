#!/usr/bin/env python3

N = int(input())

ans = 10**100

for b in range(0, 61):
    a = N // (2**b)
    c = N - (a * 2**b)
    
    ans = min(ans, a + b + c)

print(ans)

"""
while now(a,b,c) <= N:
    b += 1
    print(b)
b -= 1

print(2**29)
print(2**30)
print("----")

while now(a,b,c) <= N:
    a += 1
a -= 1

while now(a,b,c) <= N:
    c += 1
c -= 1

print(a+b+c)
"""