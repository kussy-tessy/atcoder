# print('input >>')
A, B, X = map(int, (input().split()))

left = 0
right = 10 ** 9

while True:
    middle = (left + right) // 2
    middle_cost = A * middle + B * len(str(middle))
    if middle_cost > X:
        right = middle
    elif middle_cost < X:
        left = middle
    else:
        print(middle)
        break
    if right - left == 1:
        right_cost = A * right + B * len(str(right))
        left_cost = A * left + B * len(str(left))
        if right_cost < X:
            print(right)
        else:
            print(left)
        break
        
# print('----------output----------')