import math

# print('input >>')
D, G = map(int, (input().split()))
pc = []
for _ in range(D):
    p, c = map(int, (input().split()))
    pc.append((p, c))

point = 0
ans = []

def dfs(i, count, point):
    # Gまで到達したかどうか確かめる
    c_ = count
    if point >= G:
        ans.append(count)
        return
    # 途中まで解いてGまで届くかどうか試す
    if point + (i + 1) * 100 * (pc[i][0] - 1) >= G:
        count += math.ceil((G - point) / ((i + 1) * 100))
        ans.append(count)
    # 全部解いてGまで届くかどうか試す
    elif point + (i + 1) * 100 * pc[i][0] + pc[i][1] >= G:
        count += pc[i][0]
        ans.append(count)
    if i == 0:
        return
    # 完全に解く
    dfs(i-1, c_+pc[i][0], point + (i+1)*100 * pc[i][0] + pc[i][1])
    # 完全に解かない
    dfs(i-1, c_, point)

dfs(D-1,0,0)

# print('----------output----------')
print(min(ans))