# print('input >>')

S = input()

N = len(S)

def is_kaibun(S):
    for i in range(len(S)):
        if S[i] != S[-i-1]:
            return False
    return True

if is_kaibun(S) and is_kaibun(S[:(N-1)//2]) and is_kaibun(S[(N+3)//2-1:N]):
    print('Yes')
else:
    print('No')

# print('-----output-----')

