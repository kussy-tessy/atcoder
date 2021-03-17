from collections import Counter

# print('input >>')

S = input()
S = S[::-1] + '0'

mod = 0
mods = [0] * 2019
mods[0] += 1

i_mod = 1

for i in range(len(S)-1):
    # mods[i+1] = (int(S[i+1]) * 10 ** (i+1) + mods[i]) % 2019
    i_mod %= 2019
    mod = (int(S[i]) * i_mod + mod) % 2019
    # print(mod)
    mods[mod]+=1
    i_mod *= 10

# print(mods)

ans = 0

# counter = Counter(mods)

# for n in counter.values():
#     if n > 1:
#         ans += (n * (n-1)) // 2

# print('-----output-----')

for m in mods:
    if m > 1:
        ans += (m * (m-1)) // 2

print(ans)