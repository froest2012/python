#! /usr/bin/env python3
#-*- coding: utf-8 -*-
'''
个人python算法库
'''
import pdb



#01背包问题============================================================
#arr = [509,838,924,650,604,793,564,651,697,649,747,787,701,605,644]
#v = 5000

def zeroOnePack0(cost,weight,v):
	'''
	01背包问题，未经过优化，时间O(NV)，空间f[n][v]
	'''
	n = len(cost)
	f = [[0]*v for i in range(n)]
	for i in range(n):
		for j in range(v):
			if j >= cost[i] and i > 0 and f[i-1][j] < f[i-1][j-cost[i]] + weight[i]:
				f[i][j] = f[i-1][j-cost[i]] + weight[i]
			else:
				f[i][j] = f[i-1][j]
	print(f[14][4999])

def zeroOnePack1(cost,weight,v):
	'''
	经过内存优化以后的01背包问题，时间O(NV),空间f[V]
	'''
	n = len(cost)
	f = [0 for i in range(v)]
	for i in range(n):
		for j in range(v)[::-1]:
			if j > cost[i] and  f[j] < f[j-cost[i]] + weight[i]:
				f[j] = f[j-cost[i]] + weight[i]
	print(f[4999])
#01背包问题=============================================================
if __name__ == '__main__':
	zeroOnePack1(arr,arr,v)
