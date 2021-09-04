#!/usr/bin/env python3

S = list(input())

ans = 0
alphabets = {}

for i in range(len(S)-1, 1, -1):
    s = S[i]
    # print(i)
    if not s in alphabets:
        alphabets[s] = 0
    alphabets[s] += 1
    if S[i-2] == S[i-1] and S[i-1] != S[i]:
        # print(f"{i=}で発見")
        char = S[i-2]
        if not char in alphabets:
            alphabets[char] = 0
        ans += len(S) - i - alphabets[char]
        alphabets = {}
        alphabets[char] = len(S) - i

print(ans)