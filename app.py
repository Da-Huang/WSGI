#!/usr/bin/env python
#coding: utf8

import sys
import cherrypy

class HelloWorld(object):
	@cherrypy.expose
	def index(self):
		'''
		print 'shit'
		s = 1
		for i in range(1, 100):
			for i in range(1, 100):
				for i in range(1, 100):
					s *= 21
		'''
		return 'Hello World!'


if __name__ == '__main__':
	cherrypy.quickstart(HelloWorld(), '/', 'app.conf')


