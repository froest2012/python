#! /usr/bin/env python
#http://www.practice.geeksforgeeks.org/problem-page.php?pid=302
#n的m次方得到一个数，求第k个数字是多少

num = input()
while num > 0:
	num -= 1
	a,b,k=raw_input().split( )
	a=int(a)
	b=int(b)
	k=int(k)
	s=a**b
	while k>1:
		s=s/10
		k-=1
	print s%10
