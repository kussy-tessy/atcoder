#!/usr/bin/env python3

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

N, P = map(int,(input().split()))

facts = factorization(P)

# fact_exp = [fact[1] for fact in facts]

ans = 1

# print(facts)

for fact in facts:
    f = fact[0]
    n = fact[1]
    if n >= N:
        ans *= f ** (n // N)

print(ans)