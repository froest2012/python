#! /usr/bin/env python2
# -*- coding:utf-8 -*-

import re
import traceback
import os
import os.path

"""
对日志从请求响应时间,响应结果大小,请求次数进行分析
日志格式:
'10.122.66.103 10.161.236.98 - - [24/Nov/2016:01:00:01 +0800] "GET /elasticsearch/crm/customer?param=JnVzZXJJZFNhbGVzPV5udWxsJm9yZ0lkU2FsZXM9MTM1MCwxMzA5Jm93bmVySWQ9MCZzaG9wVHlwZT0xJnN0YXJ0PTMwJnJvd3M9MTA%3D&sign=44f5e644d15fde68c9e68791ed287267 HTTP/1.0" 200 3813 22'
"""

# 请求响应时间阈值
timeThreshold = 500
# 请求响应结果阈值
resThreshold = 102400
# 请求次数阈值
callThreshold = 500


def analyzeHttpLog(logDirs):
	countDic = {}
	timeout = []
	resToBig = []
	line = ''
	for dir in logDirs:
		for fileName in os.listdir(dir):
			if os.path.isfile(os.path.join(dir, fileName)):
				print(os.path.join(dir, fileName))
				try:
					fileIn = open(os.path.join(dir, fileName), 'r')
					while True:
						line = fileIn.readline()
						if line == '':
							break
						item = analyzeLine(line)
						if item:
							if item.iname in countDic.keys():
								countDic[item.iname] += 1
							else:
								countDic[item.iname] = 0
							if int(item.time) > timeThreshold and not item.iname in timeout:
								timeout.append(item.iname)
							if int(item.res) > resThreshold and not item.iname in resToBig:
								resToBig.append(item.iname)
				except:
					print(line)
					traceback.print_exc()
				finally:
					fileIn.close()
	printCallMost(countDic)
	printTimeOut(timeout)
	printResToBig(resToBig)


def analyzeLine(line):
	if line.rfind(' 200 ') != -1:
		strArr = re.split('[ \?]', line)
		if len(strArr) > 0:
			return Item(strArr[-12], strArr[-7], strArr[-6], strArr[-2], strArr[-1])


class Item:
	"""
	每行日志对应一个这种对象,用于计算
	"""

	def __init__(self, ip, method, iname, res, time=0):
		self.ip = ip
		self.method = method
		self.iname = iname
		self.res = res
		self.time = time


def printCallMost(countDic):
	print("根据请求次数打印请求")
	sortedDics = sorted(countDic.items(), key=lambda item: item[1], reverse=True)
	for it in sortedDics:
		if it[1] > callThreshold:
			print("%s, %d" % (it[0], it[1]))


def printTimeOut(timeout):
	print("根据请求时间打印请求")
	for item in timeout:
		print(item)


def printResToBig(resToBig):
	print("根据响应结果大小打印请求")
	for item in resToBig:
		print(item)


if __name__ == '__main__':
	analyzeHttpLog([''])