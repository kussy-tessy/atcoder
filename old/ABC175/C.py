# print('input >>')
X, K, D = map(int,(input().split()))

# 0を横切らない場合
if K * D <= abs(X):
    print(abs(X) - K * D)
# 0を横切る場合
else:
    sho = abs(X) // D
    # 偶奇一致
    if sho % 2 == K % 2:
        print(abs(X) % D)
    else:
        print(abs(abs(X) % D - D))

# print('-----output-----')