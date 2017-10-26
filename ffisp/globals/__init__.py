#!/usr/bin/python
# -*- coding:utf-8 -*-

import logging
logger = logging.getLogger("django")

class GlobalMap:
	map = {'a':'a',}

	def set_map(self, key, value):
		if(isinstance(value,dict)):
			value = json.dumps(value)
		self.map[key] = value


	def set(self, **keys):
		try:
			for key_, value_ in keys.items():
				self.map[key_] = str(value_)
				logger.warn(key_+":"+str(value_))
		except BaseException as msg:
			logger.warn(msg)
			raise msg

	def del_map(self, key):
		try:
			del self.map[key]
			return self.map
		except KeyError:
			logger.warn("key:'" + str(key) + "' 不存在")

	def get(self,*args):
		try:
			dic = {}
			for key in args:
				if len(args)==1:
					dic = self.map[key]
					logger.warn(key+":"+str(dic))
				elif len(args)==1 and args[0]=='all':
					dic = self.map
				else:
					dic[key]=self.map[key]
			return dic
		except KeyError:
			logger.warn("key:'" + str(key) + "' 不存在")
			return 'Null_'

globals = GlobalMap()