#! /usr/bin/env python2
#-*- coding:utf-8 -*-

import threading
import urllib2
import pdb

max_thread = 10
lock = threading.RLock()
class download(threading.Thread):
	def __init__(self,url,start_size,end_size,fobj,buffer):
		self.url = url
		self.start_size = start_size
		self.end_size = end_size
		self.fobj = fobj
		self.buffer = buffer
		threading.Thread.__init__(self)
	def run(self):
		self.down()
	def down(self):
		req = urllib2.Request(self.url)
		req.headers['Range'] = 'bytes=%s-%s' % (self.start_size,self.end_size)
		f = urllib2.urlopen(req)
		offset = self.start_size
		while True:
			block = f.read(self.buffer)
			if not block:
				with lock:
					print('done.')
				break
			with lock:
				self.fobj.seek(offset)
				self.fobj.write(block)
				offset += len(block)
def main(url,thread = 3,save_file = '', buffer = 1024):
	thread = thread if thread < max_thread else max_thread
	req = urllib2.urlopen(url)
	size = int(req.info().getheaders('Content-Length')[0])
	fobj = open(save_file,'wb')
	avg_size,pad_size = divmod(size,thread)
	plist = []
	for i in range(thread):
		start_size = i * avg_size
		end_size = start_size + avg_size - 1
		if i == thread - 1:
			end_size = end_size + pad_size + 1
		t = download(url,start_size,end_size,fobj,buffer)
		plist.append(t)
	for p in plist:
		p.start()
	for p in plist:
		p.join()
	fobj.close()
	print('download done')
	
if __name__ == '__main__':
	url = 'ed2k://|file|%e3%80%90lol%e7%94%b5%e5%bd%b1%e5%a4%a9%e5%a0%82www.loldytt.com%e3%80%91%E8%8D%92%E9%87%8E%E7%8C%8E%E4%BA%BA.DVDScr%E4%B8%AD%E8%8B%B1%E5%8F%8C%E5%AD%97.mp4|1879205089|2A98794EB478A33B52CC6F98DF663E19|h=JFAU3AI7OV6676BZS6PF5PUYDAJZ3ISX|/'
	main(url,1,'miaowei.zip',1024)
