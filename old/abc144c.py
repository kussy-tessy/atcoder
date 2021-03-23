import math

# print('input >>')
N = int(input())

floorNsqrt = int(math.sqrt(N))

i = 0
while i <= floorNsqrt:
    i += 1
    if N % i == 0:
        N_a = i

N_b = N / N_a
ans = int(N_a-1 + N_b-1)

# print('----------output----------')
print(ans)