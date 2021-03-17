# print('input >>')
N = int(input())
As = list(map(int,(input().split())))

As.sort()
# print(As)

all_nums = [0] * (As[-1] + 1)

for A in As:
    all_nums[A] += 1

dup = 0

for i, num in enumerate(all_nums):
    if num == 0:
        continue
    if num > 1:
        dup += num
    j = 2
    while i * j <= As[-1]:
        all_nums[i*j] = 0
        j += 1
    # print(all_nums)

print(sum(all_nums)-dup)