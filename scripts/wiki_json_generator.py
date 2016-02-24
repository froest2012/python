#! /usr/bin/env python2
#-*- coding:utf-8 -*-

import urllib2
import json
import sys

'''
execute
python wiki_json_generator.py France https://en.wikipedia.org/wiki/France > China.json
python wiki_json_generator.py China https://en.wikipedia.org/wiki/China > China.json
python wiki_json_generator.py India https://en.wikipedia.org/wiki/India > India.json
python wiki_json_generator.py Japan https://en.wikipedia.org/wiki/Japan > Japan.json
python wiki_json_generator.py The_United_States https://en.wikipedia.org/wiki/United_States > United_States.json

'''
link = sys.argv[2]
htmlObj = { "link" : link ,
	"Author" : "anonymous" ,
	"timestamp" : "09-02-2014 14:16:00",
	"Title" : sys.argv[1]
	}
response = urllib2.urlopen(link)
htmlObj['html'] = response.read()
print(json.dumps(htmlObj,indent=4))
