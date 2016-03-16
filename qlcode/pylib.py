#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""个人python算法库"""
import pdb

# 01背包问题============================================================
cost = [0, 509, 838, 924, 650, 604, 793, 564, 651, 697, 649, 747, 787, 701, 605, 644]
v = 5000


# cost = [1, 2, 3, 2]
# weight = [4, 6, 12, 7]
# v = 6

# 01背包
# 使用二维数组来存储状态, 此时可以算出01背包的物品选择方案
# f[i][j] = max{f[i - 1][j],f[i - 1][j - cost[i]] + weight[i]}
def zero012(f, cost, weight, v):
	l = len(cost)
	for i in range(1, l):
		for j in range(v + 1):
			if j >= cost[i]:
				f[i][j] = max(f[i - 1][j], f[i - 1][j - cost[i]] + weight[i])
			else:
				f[i][j] = f[i - 1][j]
	print(f[l - 1][v])

# 01背包使用二维数组算出物品选择方案
def prin(f, cost, weight, i, j, l):
	if i <= 0:
		return
	if f[i][j] == f[i - 1][j - cost[i]] + weight[i]:
		l.append(i)
		prin(f, cost, weight, i - 1, j - cost[i], l)
	else:
		prin(f, cost, weight, i - 1, j, l)


# 01背包
# cost  花费
# weight    价值
# v 背包容量
# sum   所有花费总和
# 经过内存优化以后的01背包问题，时间O(NV),空间f[V]cost[i]不会影响到0~cost[i]-1,所以下界可以优化成max(v - sum(cost[i:n]),cost[i])
def pack01(cost, weight, v, sum):
	n = len(cost)
	f = [0 for i in range(v + 1)]
	for i in range(1, n):
		b = max(v - sum, cost[i])
		for j in range(b, v + 1)[::-1]:
			f[j] = max(f[j], f[j - cost[i]] + weight[i])
		sum -= cost[i]
	print(f[v])


# 01背包问题=============================================================
if __name__ == '__main__':
	sum = 0
	for i in range(len(cost)):
		sum += cost[i]
	pack01(cost, cost, v, sum)
