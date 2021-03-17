# print('input >>')
N = int(input())
check = [0] * N
nums = []
for _ in range(N):
    nums.append(int(input()))

for num in nums:
    check[num-1] += 1

try:
    x = check.index(0)
    y = check.index(2)
    print(y+1, x+1)
except:
    print('Correct')