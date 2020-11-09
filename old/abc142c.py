# print('input >>')
N = input()
A = list(map(int,(input().split())))

A_tuple_list = []

for i in range(len(A)):
    A_tuple_list.append((i, A[i]))

A_tuple_list.sort(key= lambda x:x[1])

# print('----------output----------')
for a in A_tuple_list:
    print(a[0]+1, end=' ')