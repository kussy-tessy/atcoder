#!/usr/bin/env python3

S = input()

zone = 'ZONe'

cnt = 0
for i in range(len(S)-3):
    if S[i:i+4] == zone:
        cnt += 1

print(cnt)