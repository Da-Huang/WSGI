#!/usr/bin/env python
#coding: utf8

import requests

# This is a test for wsgi
URL = 'http://localhost:9999'

if __name__ == '__main__':
	s = requests.Session()
	r = s.get(URL)
