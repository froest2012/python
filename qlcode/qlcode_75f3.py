#! /usr/bin/env python3
# -*- coding: utf-8 -*-

#超级丑，全世界没有之一
#动态规划解01背包问题，计算路径，最大收益
import pdb

v = 5000
n = 15
arr = [0,509,838,924,650,604,793,564,651,697,649,747,787,701,605,644]
f = [[0] * (v + 1) for i in range(n + 1)]
def zero012(f, cost, weight, v):
	l = len(cost)
	for i in range(1,l):
		for j in range(cost[i], v + 1)[::-1]:
			if i >= 1 and j >= cost[i]:
				f[i][j] = max(f[i - 1][j],f[i - 1][j - cost[i]] + weight[i])
	print(f[l - 1][v])
zero012(f, arr, arr, v)
