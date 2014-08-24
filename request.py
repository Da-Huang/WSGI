#/usr/bin/env python
#coding: utf8

import requests

URL = 'http://localhost:9999'

if __name__ == '__main__':
	s = requests.Session()
	for i in range(1, 100):
		r = s.get(URL)
