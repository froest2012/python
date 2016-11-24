#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import hashlib
import re

timeThreshold = 1000
resThreshold = 1048576


def analyzeHttpLog(logPaths):
	countDic = {}
	timeout = []
	resToBig = []
	for path in logPaths:
		try:
			file = open(path, 'r')
			done = 0
			while not done:
				line = file.readline()
				if line == '':
					done = 1
					break
				item = analyzeLine(line)
				if item :
					if item.iname in countDic.keys() :
						countDic[item.iname] += 1
					else:
						countDic[item.iname] = 0
					if int(item.time) > timeThreshold and not item.iname in timeout:
						timeout.append(item.iname)
					if int(item.res) > resThreshold and not item.iname in resToBig:
						resToBig.append(item.iname)
		finally:
			file.close()
	printCallMost(countDic)
	printTimeOut(timeout)
	printResToBig(resToBig)


def analyzeLine(line):
	if line.rfind(' 200 ') != -1:
		strArr = re.split('[ \?]', line)
		if len(strArr) > 0:
			return Item(strArr[0], strArr[5][1:], strArr[6], strArr[10])


class Item:
	"""
	每行日志对应一个这种对象,用于计算
	"""

	def __init__(self, ip, method, iname, res, time=0):
		self.ip = ip
		self.method = method
		self.iname = iname
		self.res = res
		hashId = hashlib.sha256()
		hashId.update(repr(iname).encode('utf-8'))
		self.hash = hashId.hexdigest()
		self.time = time


def printCallMost(countDic):
	print("根据请求次数打印请求")
	sortedDics = sorted(countDic.items(), key=lambda item:item[1], reverse=True)
	for item in sortedDics :
		print("%s, %d" % (item[0], item[1]))


def printTimeOut(timeout):
	print("根据请求时间打印请求")
	for item in timeout:
		print(item)


def printResToBig(resToBig):
	print("根据响应结果大小打印请求")
	for item in resToBig:
		print(item)


if __name__ == '__main__':
	analyzeHttpLog(['/Users/xiuc/Documents/management/search/log_analyze/search_goods_access.log'])
