print('input >>')
N = int(input())

anss = [0]*10**5
for x in range(1,101):
    for y in range(1,51):
        for z in range(1,51):
            anss[x**2+y**2+z**2+x*y+y*z+z*x] += 1

print('-----output-----')
print(anss[:N])