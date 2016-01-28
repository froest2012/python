#! /usr/bin/env python3

#超级丑，全世界没有之一
#动态规划解01背包问题，计算路径，最大收益
import pdb

v = 5000
n = 15
arr = [509,838,924,650,604,793,564,651,697,649,747,787,701,605,644]
f = [[0] * v for i in range(n+1)]
dic = {}
b = 0
ii = 0
jj = 0
for i in range(1,n+1):
	for j in range(v):
		if j >= arr[i-1] and f[i-1][j] < f[i-1][j-arr[i-1]]+arr[i-1]:
			f[i][j] = f[i-1][j-arr[i-1]]+arr[i-1]
			ijl=[]
			ijl.append(i)
			ijl.append(j)
			dic[f[i][j]] = ijl
			if j == 4999:
				b = f[i][j]
				ii = i
				jj = j
				#print("%d" %(i-1),end='-')
		else:
			f[i][j] = f[i-1][j]

while b > 0:
	print(ii,end="-")
#	pdb.set_trace()
	b = f[ii][jj]-arr[ii-1]
	if b != 0:
		ii = dic[b][0]
		jj = dic[b][1]

