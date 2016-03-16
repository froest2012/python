#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
 动态规划解01背包问题，计算路径，最大收益
"""

v = 5000
n = 15
arr = [0, 509, 838, 924, 650, 604, 793, 564, 651, 697, 649, 747, 787, 701, 605, 644]
f = [[0] * (v + 1) for i in range(n + 1)]


def zero012(f, cost, weight, v):
	l = len(cost)
	for i in range(1, l):
		for j in range(v + 1):
			if j >= cost[i]:
				f[i][j] = max(f[i - 1][j], f[i - 1][j - cost[i]] + weight[i])
			else:
				f[i][j] = f[i - 1][j]
	print(f[l - 1][v])


def prin(f, cost, weight, i, j, l):
	if i <= 0:
		return
	if f[i][j] == f[i - 1][j - cost[i]] + weight[i]:
		l.append(i)
		prin(f, cost, weight, i - 1, j - cost[i], l)
	else:
		prin(f, cost, weight, i - 1, j, l)


zero012(f, arr, arr, v)
chooseSet = []
prin(f, arr, arr, n, v, chooseSet)
print(chooseSet)
