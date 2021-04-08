#!/usr/bin/env python3

def solve(S):
    # Sがaだけで構成されているときはどうしようもない
    if all([s == 'a' for s in S]):
        return -1
    # すでに辞書順でatcoder < Sとなっているなら何もしなくてよい
    elif 'atcoder' < S:
        return 0
    # そうでないときは'a'以外の文字が初めて出現する位置を調べる
    for i, s in enumerate(S):
        if s != 'a':
            if s <= 't': # 't'より小さい文字なら先頭に持ってくればいい
                return i 
            else: # 't'より大きい文字なら先頭に持ってこずとも2文字目に持ってくればよい
                return i - 1

T = int(input())

for _ in range(T):
    print(solve(input()))