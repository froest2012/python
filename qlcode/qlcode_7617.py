#! /usr/bin/env python2
#-*- coding:utf-8 -*-

from PIL import Image

im = Image.open('lenna.png')
pix = im.load()
width = im.size[0]
height = im.size[1]
for x in range(width):
	for j in range(height):
		r, g, b = pix[x,j]
		r &= 1
		if r == 1:
			im.putpixel((x,j),(255,0,0))
		else:
			im.putpixel((x,j),(0,0,0))
im.save('7617.png')

