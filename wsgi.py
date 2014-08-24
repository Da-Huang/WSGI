#!/usr/bin/env python
#conding: utf8

import sys
import cherrypy


class HelloWorld(object):
	@cherrypy.expose
	def index(self):
		print 'shit'
		s = 1
		for i in range(1, 100):
			for i in range(1, 100):
				for i in range(1, 100):
					s *= 21
		return 'Hello World!'


application = cherrypy.Application(HelloWorld(), '/')


