#! /usr/bin/env python3
#-*- conding:utf-8 -*-

from bs4 import BeautifulSoup
import pdb

path = '/Users/xiuc/Documents/work/python/docsets/PIL.docset/Contents/Resources/Documents/index.html'
soup = BeautifulSoup(open(path),"html.parser")
alla = soup.find_all('a')
for link in alla:
	href = link.get('href')
	if href.find('pythondoc-PIL') != -1:
		fdot = href.find('.')
		ndot = href.find('.',fdot+1)
#		pdb.set_trace()
		name = href[fdot+1:ndot]
		print("INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES ('%s', '%s', '%s');" %(name,'Keyword',href))
