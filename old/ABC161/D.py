lunluns = []

def dfs(n, cur):
    global lunluns
    lunluns.append(int(n))
    if cur > 8:
        return
    if n[-1] == '0':
        dfs(n+'0', cur+1)
        dfs(n+'1', cur+1)
    elif n[-1] == '9':
        dfs(n+'8', cur+1)
        dfs(n+'9', cur+1)
    else:
        last = int(n[-1])
        dfs(n + str(last-1), cur+1)
        dfs(n + str(last), cur+1)
        dfs(n + str(last+1), cur+1)

for i in range(1,10):
    dfs(str(i), 0)

K = int(input())
lunluns.sort()
print(lunluns[K-1])