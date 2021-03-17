#!/usr/bin/env python3


N, K = map(int,(input().split()))

ans = 0

# a % bでbを固定しながらaを1から増やしていく。すべてのbについてローラーする
for b in range(1, N+1):
    # print(f'{b=}')
    # 1周期の中に何回あるか
    per_cycle = max(0, b - K)
    cycles = N // b
    # print(f'{per_cycle=}, {cycles=}')
    # 余った周期
    rest = max(0, N % b - max(0, (K - 1)))
    # print(f'{rest=}')
    ans += per_cycle * cycles + rest

print(ans)
