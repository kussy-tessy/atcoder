A, B, C =  map(int,(input().split()))
s = set([A, B, C])
print('Yes') if len(s) == 2 else print('No')