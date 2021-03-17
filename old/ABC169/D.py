# print('input >>')
N = int(input())
ans = 0

p = 2
e = 1
z = lambda p, e: p ** e

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

kake = 1

should_break = False

# z = 1

"""
while N > 1:
    # print(N)
    if N % z == 0:
        ans += 1
        N //= z 
    z += 1
    if z > N:
        break

print(ans-1)

"""
while N > 1 and not should_break:
    print(N)
    e = 1
    while N % z(p,e) == 0:
        if N % z(p,e) == 0:
            ans += 1
            N //= z(p,e)
            kake *= z(p,e)
            e += 1
    while True:
        p += 1
        if is_prime(p):
            break
    if is_prime(N):
        should_break = True
        ans += 1

# print('-----output-----')
# print(ans)