#! /usr/bin/env python2
#-*- coding:utf-8 -*-

import threading
import urllib2
import pdb

max_thread = 10
lock = threading.RLock()
class download(threading.Thread):
	def __init__(self,url,start_size,end_size,fobj,buffer,headers):
		self.url = url
		self.start_size = start_size
		self.end_size = end_size
		self.fobj = fobj
		self.buffer = buffer
		self.headers = headers
		threading.Thread.__init__(self)
	def run(self):
		self.down()
	def down(self):
		req = urllib2.Request(self.url)
		for key,value in self.headers.items():
			req.headers[key] = value
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
def main(url,thread = 3,save_file = '', buffer = 1024,headers = {}):
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
		t = download(url,start_size,end_size,fobj,buffer,headers)
		plist.append(t)
	for p in plist:
		p.start()
	for p in plist:
		p.join()
	fobj.close()
	print('download done')
	
if __name__ == '__main__':
	url = 'http://lx.cdn.baidupcs.com/file/8f87d3ca09c7c0e9bb0f02f5f3304085?bkt=p2-qd-900&xcode=7b349733c15203da27ede9c08cb49d416d5a0eb659e9a7c4d796109456bd1356&fid=4046605047-250528-476091433617476&time=1456812140&sign=FDTAXGERLBH-DCb740ccc5511e5e8fedcff06b081203-Iz%2F4axuP%2BX7VPrkh2QGh%2B8t7vkM%3D&to=lc&fm=Qin,B,T,t&sta_dx=355&sta_cs=260&sta_ft=mov&sta_ct=7&fm2=Qingdao,B,T,t&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=14008f87d3ca09c7c0e9bb0f02f5f3304085896837f60000162f2dc9&sl=73400398&expires=8h&rt=sh&r=997524542&mlogid=1405136173310980571&vuk=1410219715&vbdid=2717433831&fin=1-%E8%BF%90%E7%AE%97%E7%AC%A6%E3%80%81%E7%A8%8B%E5%BA%8F%E6%B5%81%E7%A8%8B%E6%8E%A7%E5%88%B6%EF%BC%88%E4%B8%8A%EF%BC%89.mov&fn=1-%E8%BF%90%E7%AE%97%E7%AC%A6%E3%80%81%E7%A8%8B%E5%BA%8F%E6%B5%81%E7%A8%8B%E6%8E%A7%E5%88%B6%EF%BC%88%E4%B8%8A%EF%BC%89.mov&slt=pm&uta=0&rtype=1&iv=0&isw=0&dp-logid=1405136173310980571&dp-callid=0.1.1'
	headers = {
			'Cookie':'BIDUPSID=AF19A83AD6B22BEBDD8024D6ECDB1A16; PSTM=1446623926; PANWEB=1; bdshare_firstime=1449801291319; Hm_lvt_773fea2ac036979ebb5fcc768d8beb67=1451730553; BAIDUID=B064DDE01F09FF04D76E4789AB199AE8:FG=1; MCITY=-179%3A; BDSFRCVID=qALsJeC62xEKrr54z5Unt8Acwe5EbWJTH6ao0rb3sTi22tL0AFMGEG0PJOlQpYD-2izaogKKKgOTHI6P; H_BDCLCKID_SF=tJuHoCKyfCvbfP0khtO-hPRH-UnLqMrB257Z0l8KtDbYehnT56O-jPKt5a7C5bb-aCjy-IQmWIQHDPohhR50jpKuXpuOJPoz3mb4KKJxbIOSVtJXQKc10fAthUJiBMnMBan7aCQxfD05bDI9D5-35n-Wqxv8etJyaR3HKx7bWJ5TMC_m0pLhMtR35xr0an0O0C7f0R6EaM--ShPC-tnDhxKmjxO7K-_tbn675-nJ3l02V-bChhQ2Wf3DMMnne4RMW23i0h7mWpI-VKF6DTuBe5OyepJf-K6QM4o2WbCQbpOTqpcNLTDKjhtujfrytn502moJVpjJbb5VDJ72jlO1j4_e-xTly55bWIvK_4-hWpOWHp5jDh3M54AuKbrRe4vyQPjy0hvcWb3cShnVjl00jTJ-eHAjJ5nfb5kXWPI8Kb7VbnbgynbkbfJBDGOgQ6Q0abnqBxcGbInNHP3Nhtco35K7yajK2-jX3H8q0pnjKC5MhqnJ2-bpQT8r5hjQQROk3Pj3WM-Eab3vOpvTXpO1yjKreGKDqTLDJnIsL-35HJRBKROvhjRA0q4yyxomtjjCtgOkVn82bJTjMt-9Ltbbbjv-WRnyLUkqKCO9XJONMRcOj-O4BPKa3P33QttjQn0eaN6jhl-EWp6R8J7TyURvbU47y-uqQTIDtnuHVIt5tDvbfP0kb-QKKRFXMfTMetJyaR3k_t5bWJ5TMCo-0j8K-4635l5B3b0O0C7f0lvq2hF5ShPC-tPbyj_jQpKLabQ8Wj7rQKTv3l02VhFRhhQ2Wf3DQxoBb4RMW23i0h7mWpI-VKFCjTu2Dj3QeUcQ-nJLHjnL3RRsHJOoDDvlLfv5y4LdjG5O0xnH-JIJXD5Gat-WEJO6bjop-l-p3-Aq544j-DueQMbVtDoM8KJqQxcnQfbQ0-692pojymPLoJTLKR7JOpvobUnxyMcB0a62btt_tbAeVxK; BDUSS=klxTGFKcmRNT0N6TjFVMH5HWn40R1o2YXpIT2VFM1B1T2Vvakk5U3E1UGcxflJXQVFBQUFBJCQAAAAAAAAAAAEAAABwVBwKZnJvZXN0MjAxMgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOBKzVbgSs1WQ; Hm_lvt_adf736c22cd6bcc36a1d27e5af30949e=1456295033,1456802492; Hm_lpvt_adf736c22cd6bcc36a1d27e5af30949e=1456802990; BDCLND=wc8m4ioj642M%2FzW1hxejAw%2F7DuIIepnWVU%2FsbroMqdA%3D; H_PS_PSSID=17745_1427_18241_18205_17000_17073_14976_12405_18837_10633; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1456802335,1456802340,1456802346,1456802492; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1456813092',
			'Host':'pan.baidu.com',
			'Refer':'http://pan.baidu.com/share/link?shareid=2312390392&uk=4046605047',
			'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
			'Connection':'keep-alive',
			'Accept-Encoding':'gzip, deflate, sdch'
			}
	main(url,1,'miaowei.zip',1024,headers)
