#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import requests
import time
import pdb
from urllib import quote

proxys = [
	{'http':'128.199.177.165:8080'},
	{'http':'37.187.144.131:8888'},
	{'http':'121.10.234.15:3128'},
	{'http':'113.248.233.199:8998'},
	{'http':'217.27.40.94:8080'},
	{'http':'222.188.88.10:8998'},
	{'http':'111.204.0.254:9999'},
	{'http':'177.44.130.6:8080'},
	{'http':'183.140.82.153:3128'},
	{'http':'148.251.132.176:10000'},
	{'http':'13.93.222.78:80'},
	{'http':'31.134.92.56:3128'},
	{'http':'119.135.185.99:9999'},
	{'http':'58.8.196.132:8888'},
	{'http':'189.81.77.136:8080'},
	{'http':'5.9.117.40:3128'},
	{'http':'195.83.72.92:8080'},
	{'http':'1.48.145.180:81'},
	{'http':'36.234.116.31:808'},
	{'http':'83.142.165.162:8080'},
	{'http':'182.89.6.40:8123'},
	{'http':'109.201.108.77:8080'},
	{'http':'101.51.135.34:8080'},
	{'http':'177.57.240.239:8080'},
	{'http':'202.118.8.13:3128'},
	{'http':'2.233.122.48:3128'},
	{'http':'110.78.152.18:8080'},
	{'http':'149.56.13.5:5555'},
	{'http':'91.185.3.222:8080'},
	{'http':'123.56.74.13:8080'},
	{'http':'154.118.247.90:8080'},
	{'http':'218.66.253.144:8800'},
	{'http':'62.148.92.210:8080'},
	{'http':'113.79.35.68:8118'},
	{'http':'183.140.85.223:3128'},
	{'http':'178.62.53.162:8888'},
	{'http':'179.179.136.49:8080'},
	{'http':'218.106.205.145:8080'},
	{'http':'111.132.254.35:81'},
	{'http':'113.124.248.2:1337'},
	{'http':'112.118.43.137:3128'},
	{'http':'45.55.216.52:3128'},
	{'http':'115.24.189.20:8998'},
	{'http':'36.97.145.29:9999'},
	{'http':'37.79.251.212:8080'},
	{'http':'90.161.32.140:3128'},
	{'http':'193.34.13.188:8080'},
	{'http':'88.119.17.195:8080'},
	{'http':'185.50.169.111:8080'},
	{'http':'14.211.61.116:9797'},
	{'http':'14.119.41.219:8080'},
	{'http':'62.209.227.242:8080'},
	{'http':'220.136.21.161:8080'},
	{'http':'188.168.247.80:8080'},
	{'http':'91.238.254.122:8080'},
	{'http':'1.197.59.185:808'},
	{'http':'115.28.20.126:3128'},
	{'http':'123.13.204.139:9797'},
	{'http':'112.118.203.40:3128'},
	{'http':'121.32.118.19:9797'},
	{'http':'183.19.42.178:3128'},
	{'http':'109.228.138.216:3128'},
	{'http':'171.13.208.54:9797'},
	{'http':'125.118.47.108:9999'},
	{'http':'88.82.93.98:8080'},
	{'http':'115.226.10.175:8888'},
	{'http':'217.150.52.221:8123'},
	{'http':'117.66.123.219:808'},
	{'http':'106.115.191.55:9999'},
	{'http':'157.100.180.14:8080'},
	{'http':'60.249.13.250:3128'},
	{'http':'110.179.54.98:8888'},
	{'http':'58.242.248.5:80'},
	{'http':'39.89.68.59:81'},
	{'http':'175.182.128.194:8080'},
	{'http':'14.120.176.94:9999'},
	{'http':'175.42.46.175:8888'},
	{'http':'115.218.231.117:8888'},
	{'http':'46.105.152.80:8888'},
	{'http':'123.121.136.79:9999'},
	{'http':'203.202.251.42:8080'},
	{'http':'117.57.63.120:808'},
	{'http':'113.79.74.196:9797'},
	{'http':'175.171.55.49:8888'},
	{'http':'87.116.201.201:8080'},
	{'http':'111.250.43.164:8080'},
	{'http':'122.228.179.178:80'},
	{'http':'122.154.100.164:8080'},
	{'http':'220.137.41.221:8080'},
	{'http':'145.236.103.67:3128'},
	{'http':'178.33.4.48:3128'},
	{'http':'113.110.174.128:9999'},
	{'http':'220.135.150.211:3128'},
	{'http':'5.1.50.138:8080'},
	{'http':'115.238.228.9:8080'},
	{'http':'188.168.26.0:8080'},
	{'http':'121.8.170.53:9797'},
	{'http':'202.57.10.117:8080'},
	{'http':'178.49.228.101:3128'},
	{'http':'46.170.112.86:8080'}
]

fileArr = ['suggestRes1.log','suggestRes2.log','suggestRes3.log','suggestRes4.log','suggestRes5.log','suggestRes6.log','suggestRes7.log','suggestRes8.log','suggestRes9.log','suggestRes10.log']
outFile = '/Users/xiuc/Downloads/suggestOutJd.log'
outFileTb = '/Users/xiuc/Downloads/suggestOutTb.log'

def scrap(fileArr, flag) :
	for file in fileArr:
		print(file)
		fileName = '/Users/xiuc/Downloads/'+file
		if flag == 'jd' :
			scrapJd(fileName, outFile)
		else:
			scrapTb(fileName, outFileTb)


def scrapJd(fileName, outFile) :
	file = open(fileName, 'r')
	fileOut = open(outFile, 'a')
	done = 0
	while done == 0 :
		# pdb.set_trace()
		line = file.readline().strip()
		if line == '':
			break
		# line = '219 1210100211'
		arr = line.split(" ")
		url='https://dd-search.jd.com/?ver=2&zip=1&key=' + quote(arr[1]) + '&pvid=iz5h7fui.ffg5gl&t=1476779775036&curr_url=www.jd.com%2F&callback=jQuery9192176'
		headers={
			"Accept":"*",
			"Accept-Encoding" :"gzip, deflate, sdch, br",
			"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
			"Cache-Control":"no-cache",
			"Connection":"keep-alive",
			"Cookie":"user-key=b6fdfb64-4cb6-43dd-b8ff-bfc8557d6195; TrackID=17mbus9ndv8HqU738kG6sEVBYD8jjNossI_JFTeToA2MvpjEK8lqye3gqNHfqSntHx4Gy9Cy7DWZiNsidY0PGhiLJVhHsXOPFV_YAhmPpNBWHp5VJ_59pVNSVjm_TVx2n; pinId=6PYyMg9Le9HdyDu6-RrCQQ; unick=%E7%A7%80%E5%B7%9D%E7%A5%9E; _tp=BL2O8kpzoJEJVG2AcOKhug%3D%3D; _pst=13735884683_p; mt_xid=V2_52007VwMRWlpQUlMfShtsAWcEFlBeCAZGGh4QXxliBRIGQQsAXEtVH1pWZQQQB1hRUAhKeRpdBWAfElNBWFNLHEoSWAVsAhtiX2hSah9IGlgNYwcUYl1dVF0%3D; areaId=15; unpl=V2_ZzNtbUEEFkUiXREEeh1dBGILEQ8SVRBHIV9GV3McCQUwCkVfclRCFXIURlVnGVgUZwUZXEJcQRJFCHZXfBpaAmEBFl5yAR1LI1USECRBAloJChFbS1FEE30JQVdLKV8FVwMTbUJUSxJ9CE9UeBtsNWAzEl9AU0AQdTh2UnwaWQNuMxNtQ2cBQSkBR1F9Gl1IZwAaWkpXShV2CnZVSxo%3d; __jdv=122270672|google-union|t_262767352_googleunion|cpc|82787679062_0_2bdafdfa0500492ca3bcef1294d1f8f3|1476522101302; ipLoc-djd=15-1213-1214-0; ipLocation=%u6D59%u6C5F; cn=0; __jda=122270672.1296918123.1446681761.1476747218.1476777975.111; __jdb=122270672.1.1296918123|111.1476777975; __jdc=122270672; __jdu=1296918123",
			"Host":"dd-search.jd.com",
			"Pragma":"no-cache",
			"Referer":"https://www.jd.com/",
			"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"

		}
		content=requests.get(url=url, headers=headers, proxies=proxys).content
		fileOut.write(arr[1] + ' ' + content[len('jQuery9192176') + 1:-1])

def scrapTb(fileName, outFile) :
	file = open(fileName, 'r')
	fileOut = open(outFile, 'a')
	done = 0
	while done == 0 :
		# pdb.set_trace()
		line = file.readline().strip()
		if line == '':
			break
		# line = '219 205'
		arr = line.split(" ")
		url='https://suggest.taobao.com/sug?code=utf-8&q=' + quote(arr[1]) + '&_ksTS=1476859491303_1451&callback=jsonp1452&k=1&area=c2c&bucketid=5'
		headers={
			# ":authority":"suggest.taobao.com",
			# ":method":"GET",
			# ":path":"/sug?code=utf-8&q=" + quote(arr[1]) + "&_ksTS=1476859491303_1451&callback=jsonp1452&k=1&area=c2c&bucketid=5",
			# ":scheme":"https",
			"accept":"*/*",
			"accept-encoding" :"gzip, deflate, sdch, br",
			"accept-language":"zh-CN,zh;q=0.8,en;q=0.6",
			"cache-control":"no-cache",
			"cookie":"thw=cn; cna=hqrADmXcEB0CAX1569UIgp3s; lzstat_uv=27383024923531600901|3492151@3600092@3176362@3073248; miid=8304319208266887590; ucn=unsz; hng=CN%7Czh-cn%7CCNY; v=0; _tb_token_=e37eee38e3db7; uc3=sg2=AQcn7EsJfhKv2pH%2Fx1gj%2BSFOF%2BA5Szf2X70Y5TpU8ic%3D&nk2=BcLFm6KQ3FVn&id2=UoM4a4siFZ5x&vt3=F8dAS18yyznoxP8YtlU%3D&lg2=VFC%2FuZ9ayeYq2g%3D%3D; existShop=MTQ3Njg0NTQ1Ng%3D%3D; uss=UNDcG78ATE3LVkQ9Z6grgsGcCWtUvIO5BMQbbvRhR5v1Xq38cf1t%2Fia2Cw%3D%3D; lgc=froestsen; tracknick=froestsen; mt=np=&ci=10_1&cyk=0_0; skt=89faad48755d3fd0; _cc_=URm48syIZQ%3D%3D; tg=0; cookie2=1cc16846ecc96cc6e258920522985f6e; t=1e5432df00793324ea19ed83ccc957fc; isg=AvLyOmK2_gpOlM1EIs2Lg1_FQz4fi2EyePwBaLzLnqWRT5BJoBE-LZRpSVyJ; l=AkFBqKtDXCIfhBnf-G91/wFZ0Ydb7rVh",
			"pragma":"no-cache",
			"referer":"https://www.taobao.com/",
			"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"

		}
		content=requests.get(url=url, headers=headers, proxies=proxys).content.strip()
		fileOut.write(arr[1] + ' ' + content[len('jsonp1452') + 1:-1] + '\n')

'''
	爬去京东分类
'''
def scrapJdCate(outFile) :
	fileOut = open(outFile, 'a')
	url='https://dc.3.cn/category/get?callback=getCategoryCallback'
	headers={
		"Accept":"*/*",
		"Accept-Encoding" :"gzip, deflate, sdch, br",
		"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
		"Cache-Control":"no-cache",
		"Connection":"keep-alive",
		"Host":"dc.3.cn",
		"Pragma":"no-cache",
		"Referer":"https://www.jd.com/",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"

	}
	content=requests.get(url=url, headers=headers, proxies=proxys).content
	fileOut.write(content[len('getCategoryCallback') + 1:-1])

# scrap(fileArr, 'jd')
# scrap(fileArr, 'tb')
scrapJdCate('/Users/xiuc/Downloads/suggestOutJdCate.log')