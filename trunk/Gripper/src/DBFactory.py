# -*- coding: gbk -*- 
'''
Created on 2010-11-25

@author: cg
'''
from GuitarTabGripperDB import *

'''
数据库连接参数
'''
DBParam = {"addr":"221.122.122.110" ,
           "port":3306,
           "user":"xxx",
           "pw":"xxx",
           "db":"tabs" }

'''
数据库适配器工厂类
'''
def GetDBAdapter():
    db = GuitarGripperDBAdapter()
    db.connect(DBParam["addr"], DBParam["port"], DBParam["user"], DBParam["pw"], DBParam["db"])
    return db

if __name__ == '__main__':
    a = GetDBAdapter()