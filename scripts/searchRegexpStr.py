#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os

'''从文件读入数据,通过正则表达式对文件进行查找,输出匹配的字符串'''

inputFile1 = open('/Users/xiuc/Downloads/tmp2')
inputFile2 = open('/Users/xiuc/Downloads/tmp3')
outFile11 = open('/Users/xiuc/Downloads/tmp5', 'wb')
outFile22 = open('/Users/xiuc/Downloads/tmp6', 'wb')
try:
     all_the_text1 = inputFile1.read()
     all_the_text2 = inputFile2.read()
finally:
     inputFile1.close()
     inputFile2.close()
p = re.findall('"customer_id":.\d*', all_the_text1)
for str in p:
     outFile11.writelines(str+'\r\n')
outFile11.close()

p = re.findall('"customer_id":.\d*', all_the_text2)
for str in p:
     outFile22.writelines(str+'\r\n')
outFile22.close()

os.system('diff /Users/xiuc/Downloads/tmp5 /Users/xiuc/Downloads/tmp6 > /Users/xiuc/Downloads/tmp9')

