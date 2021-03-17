print('input >>')
K = int(input())

for i in range(1, K):
    bai = K * i
    if all([s == '7' for s in str(bai)]):
        print(bai) 

print('-----output-----')