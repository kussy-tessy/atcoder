import math

# print('input >>')
A, B, H, M = map(int,(input().split()))

PI = math.pi

tan_deg = H / 12 * (2 * PI) + M / 60 * (PI / 6) 
chou_deg = M / 60 * (2 * PI)

kakudo = abs(chou_deg-tan_deg)

C2 = A**2 + B**2 - 2*A*B * math.cos(kakudo)

ans = math.sqrt(C2)

# print('-----output-----')
print(ans)