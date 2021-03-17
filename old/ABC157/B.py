# print('input >>')
As = []
As += list(map(int,(input().split())))
As += list(map(int,(input().split())))
As += list(map(int,(input().split())))
N = int(input())
bingo = [0] * 9
for b in range(N):
    b = int(input())
    if b in As:
        bingo[As.index(b)] = 1    

# print('-----output-----')
if bingo[0]*bingo[1]*bingo[2] == 1 or bingo[3]*bingo[4]*bingo[5] == 1 or bingo[6]*bingo[7]*bingo[8] == 1 or bingo[0]*bingo[3]*bingo[6] == 1 or bingo[1]*bingo[4]*bingo[7] == 1 or bingo[2]*bingo[5]*bingo[8] == 1 or bingo[0]*bingo[4]*bingo[8] == 1 or bingo[2]*bingo[4]*bingo[6] == 1:
    print('Yes')
else:
    print('No')
