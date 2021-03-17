# print('input >>')
A, B, C, D = map(int,(input().split()))

takahashi = A
aoki = C

while takahashi > 0 and aoki > 0:
    aoki -= B 
    takahashi -= D

if aoki <= 0:
    print('Yes')
else:
    print('No')

# print('-----output-----')