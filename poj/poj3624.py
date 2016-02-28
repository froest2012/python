#! /usr/bin/env python
# -*- coding:utf-8 -*-

def zeroOnePack(cost, weight, v, b, f):
    for j in range(b, v+1)[::-1]:
        f[j] = max(f[j],f[j - cost] + weight)

def zeroOnePack1(cost, weight, v):
    n = len(cost)
    f = [0 for i in range(m+1)]
    for i in range(n):
        b = max(v - sum(cost[i:n]), cost[i])
        for j in range(b, m+1)[::-1]:
            f[j] = max(f[j],f[j - cost[i]] + weight[i])
    print(f[m])

n, m = map(int,raw_input().split(' '))

weight = [0 for i in range(n)]
cost = [0 for i in range(n)]
s = 0
for i in range(n):
    cost[i], weight[i] = map(int,raw_input().split(' '))

zeroOnePack1(cost,weight,m)
