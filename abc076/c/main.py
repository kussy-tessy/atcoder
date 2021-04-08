#!/usr/bin/env python3

S = input()
T = input()

hit = []

for i in range(len(S)-len(T)+1):
    s = S[i:i+len(T)]
    is_ok = True
    for s_, t_ in zip(s, T):
        if not(s_ == '?' or s_== t_):
            is_ok = False
    if is_ok:
        hit.append(i)

if len(hit) == 0:
    print('UNRESTORABLE')
else:
    hit_i = hit[-1]
    for i, s in enumerate(S):
        if hit_i <= i < hit_i+len(T):
            # print(i-hit_i)
            print(T[i-hit_i], end='')
        elif s == '?':
            print('a', end='')
        else:
            print(s, end='')
    print()