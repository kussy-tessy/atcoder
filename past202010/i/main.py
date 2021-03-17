#!/usr/bin/env python3

print('input >>')
N = input()
al = list(map(int,(input().split())))
al += al
gokei = sum(al) / 2

for i in range(len(al)):
    res = 10 ** 10
    for left in range(len(al)):
        right = 0
        eat = 0
        not_eat = gokei - eat
        diff = abs(eat - not_eat)
        now_diff = diff
        while True:
            print(left, right)
            eat += al[i]
            right += 1
            not_eat = gokei - eat
            now_diff = abs(eat - not_eat)
            print(now_diff, diff)
            if now_diff > diff:
                break
        res = min(res, now_diff)

print('-----output-----')
print(res)