#!/usr/bin/env python3
from collections import defaultdict

N = int(input())
As = list(map(int,(input().split())))

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
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

"""pair_a = []
pair_b = []

for i in range(N // 2):
    a = As[i]
    b = As[N-1-i]
    if a != b:
        pair_a.append(min(a, b))
        pair_b.append(max(a, b))

print(min(len(set(pair_a)), len(set(pair_b))))"""

# pairs = []

uf = UnionFind(2*10**5+1)

for i in range(N // 2):
    a = As[i]
    b = As[N-1-i]
    if a != b:
        uf.union(a, b)

uf_all = uf.all_group_members()

ans = 0
for u in uf_all.values():
    ans += len(u)-1

print(ans)