#coding=utf-8
#author：zwx
from pymongo import MongoClient
from pymongo import InsertOne
import time

# 连接数据库服务器
conn = MongoClient("mongodb://192.168.18.163:27018", maxPoolSize=None)
class dataRunMain():
	#添加
	def insert(self):
		#连接数据库xx数据库，没有则自动创建
		db=conn.zwxtest
		# 使用test表，没有则自动创建
		my_set = db.test
		#插入数据
		my_set.insert({"name": "zhangsan", "age": 18})

	#删除
	def delete(self):
		db = conn.zwxtest#conn.数据库
		my_set = db.test#db.数据库表名

		my_set.remove({'name': 'zhangsan'})

if __name__ == '__main__':
	dataRunMain().insert()