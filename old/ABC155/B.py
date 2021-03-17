# print('input >>')
N = int(input())
As = list(map(int,(input().split())))
As_even = [e for e in As if e % 2 == 0]

for A in As_even:
    if not(A % 3 == 0 or A % 5 == 0):
        print('DENIED')
        exit()
        
# print('-----output-----')
print('APPROVED')