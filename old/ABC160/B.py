# print('input >>')
X = int(input())

happiness = 0

gohyaku = X // 500
happiness += gohyaku * 1000
X -= 500 * gohyaku
go = X // 5
happiness += go * 5

# print('-----output-----')
print(happiness)