#!/usr/bin/env python3

t, N = map(int,(input().split()))

kake = []
prev = 0
for i in range(101):
    en = i * (100 + t)
    # print(en, en // 100, prev + 1)
    if en // 100 != prev + 1:
        kake.append(en // 100 - 1)
    prev = en // 100

sento = kake[1:(t+1)]
# print(sento)
next_top = kake[t]
diff = next_top + 1

# print(f'{sento=}')
row = (N-1) // t
col = N % t
# print(f'{row=},{col=}')
ans = sento[col-1] + row * diff
print(ans)
# print([kake[i+1] - kake[i] for i in range(len(kake)-1)])