#!/usr/bin/env python3

from math import gcd

# いやああ無理だーーーー
# これ一次不定方程式の整数解を求めればいいんだよね？？？

# 記念提出

# https://qiita.com/DaikiSuyama/items/3687e9f2fa3ed097e2fc
# なんか違う気がする……。
class LDE:
    #初期化
    def __init__(self,a,b,c):
        self.a,self.b,self.c=a,b,c
        self.m,self.x0,self.y0=0,[0],[0]
        #解が存在するか
        self.check=True
        g=gcd(self.a,self.b)
        if c%g!=0:
            self.check=False
        else:
            #ax+by=gの特殊解を求める
            self.extgcd(self.a,self.b,self.x0,self.y0)
            #ax+by=cの特殊解を求める
            self.x0=self.x0[0]*c//g
            self.y0=self.y0[0]*c//g
            #一般解を求めるために
            self.a//=g
            self.b//=g

    #拡張ユークリッドの互除法
    #返り値:aとbの最大公約数
    def extgcd(self,a,b,x,y):
        if b==0:
            x[0],y[0]=1,0
            return a
        d=self.extgcd(b,a%b,y,x)
        y[0]-=(a//b)*x[0]
        return d

    #パラメータmの更新(書き換え)
    def m_update(self,m):
        self.x0+=(m-self.m)*self.b
        self.y0-=(m-self.m)*self.a
        self.m=m

def calc(N, S, K):
    # 割り切れるとき
    if N % K == 0:
        # いけるとき
        if (N - S) % K == 0:
            return (N - S) // K
        # あかんとき
        else:
            return -1
    # 割り切れないとき
    else:
        lde = LDE(N, -K, S)
        print()

# T = int(input())
# queries = []

# for _ in range(T):
#     queries.append(list(map(int,(input().split()))))

# N, K, S = 998244353, 897581057, 595591169
# N, K, S = 10000, 6, 14
# # lde = LDE(N, -S, K)
# lde = LDE(10000, -14, 6)

# print(lde.b)
# print(lde.a)
# print(lde.y0)
# print(lde.x0)

for query in queries:
    print(calc(query[0], query[1], query[2]))

