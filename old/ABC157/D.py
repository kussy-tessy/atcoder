# https://note.nkmk.me/python-union-find/
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

# print('input >>')
N, M, K = map(int,(input().split()))
friend_numbers = [0] * N
block_numbers = [0] * N # ただし同じUnionFind木内のみ
unionFind = UnionFind(N)
for _ in range(M):
    friend = list(map(int,(input().split())))
    i = friend[0]-1
    j = friend[1]-1
    unionFind.union(i, j)
    friend_numbers[i] += 1
    friend_numbers[j] += 1
for _ in range(K):
    block = list(map(int,(input().split())))
    i = block[0]-1
    j = block[1]-1
    if unionFind.same(i, j):
        block_numbers[i] += 1
        block_numbers[j] += 1

# print(friend_numbers)
# print(block_numbers)
# print(unionFind)

for i in range(N):
    print(unionFind.size(i) - friend_numbers[i] - block_numbers[i] - 1, end=' ')    

# print('-----output-----')