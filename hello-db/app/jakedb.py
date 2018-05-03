# -*- coding: utf-8 -*-
# @Author: Jacob Schwartz
# @Date:   2018-05-03 11:50:04
# @Last Modified by:   Jacob Schwartz
# @Last Modified time: 2018-05-03 12:33:54

################################
### DO NOT EDIT FOR TUTORIAL ###
################################

from tinydb import TinyDB, Query

class JakeDB():
	def __init__(self, path):
		self.db = TinyDB(path)

	def insert(self, name, **kwargs):
		# name must unique 
		if self.exists(name):
			return -1
		dict = {'name': name}
		for key, value in kwargs.items():
			dict[key] = value
		return self.db.insert(dict)

	def get(self, name):
		return self.db.search(Query().name == name)

	def delete(self, name):
		return self.db.remove(Query().name == name)

	def update(self, name, **kwargs):
		self.delete(name)
		self.insert(name, **kwargs)

	def exists(self, name):
		if len(self.get(name)) == 0:
			return False
		return True

	def get_all(self):
		return self.db.all()

	def delete_all(self)
		return self.db.purge()