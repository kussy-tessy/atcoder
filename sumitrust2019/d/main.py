N = int(input())
S = input()

indices = {}

for i, s in enumerate(S):
    if not s in indices:
        indices[s] = []
    indices[s].append(i)

# 1桁目xとしてありうる数字は、min(i) < N-3までの数字
ans = 0
for x in indices:
    if min(indices[x]) <= N-3:
        # 2桁目yとしてありうる数字は、max(i) > 1桁目xのidxの最小値 かつ min(i) < N-2までの数字
        x_idx = min(indices[x])
        for y in indices:
            if max(indices[y]) > x_idx and min(indices[y]) <= N-2:
                # 3桁目zとしてありうる数字は、max(i) > 2桁目yのidxの数字
                y_idx = min([idx for idx in indices[y] if idx > x_idx])
                for z in indices:
                    if max(indices[z]) > y_idx:
                        ans += 1

print(ans)