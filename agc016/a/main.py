#!/usr/bin/env python3

s = input()

# 馬鹿みたいに総当りして全部試す(N<100だから)
chars = set(s)

if len(chars) == 1:
    print(0)
    exit()

ans = 1000
for char in chars:
    # print(char)
    cnt = 0
    old_str = s
    is_ok = False
    while not is_ok:
        is_ok = True
        cnt += 1
        new_str = ''
        for i in range(1, len(old_str)):
            if old_str[i-1] == char or old_str[i] == char:
                new_str += char
            else:
                new_str += old_str[i-1]
                is_ok = False
        old_str = new_str
        # print(new_str)
    ans = min(ans, cnt)
        
print(ans)