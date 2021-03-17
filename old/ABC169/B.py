import sys

# print('input >>')
N = int(input())
As = list(map(int,(input().split())))

INF = 10 ** 18

ans = 1

over = False

for A in As:
    if A == 0:
        print(0)
        sys.exit()

for A in As:
    ans *= A
    if ans > INF:
        print(-1)
        sys.exit()
        
# print('-----output-----')
print(ans)
