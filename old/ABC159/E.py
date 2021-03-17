import itertools as it

def count(H, left_i, i):


print('input >>')
H, W, K = map(int,(input().split()))
Ss = [input() for _ in range(H)]

# Hの割り方を決める
Hs = it.product([0,1], repeat=H-1)

for H in Hs:
    Hcut = [i for i, h in enumerate(H) if h==1]
    print(Hcut)
    for i in range(len(Ss)): 
        max_ = 0
        


print('-----output-----')

# 僕には難しすぎた……。