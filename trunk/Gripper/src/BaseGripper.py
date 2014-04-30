# -*- coding: gbk -*- 
'''
Created on 2010-10-12

@author: cg
'''

import re
import DBFactory
from page_grip_helper.DB import *
from page_grip_helper.PageGripper import *
from page_grip_helper.Tools import *
from GuitarTabGripperDB import *


TAB_TYPE = {'UNKNOW':0,
            'TXT':1,
            'IMAGE':2,
            'GTP':3
            }

DEBUG = False

class BaseGripper():
    def __init__(self):
        self.totalNew = 0
        self.gripper = PageGripper()
        self.db = DBFactory.GetDBAdapter()
        
    def findTab(self,artist,title,type,ref_url,localPath):
        print "歌手:%s, 歌名:%s, 谱类型:%s, url:%s"%(artist,title,type,ref_url)
        if DEBUG==False and self.db.updateTab(title, artist, type, ref_url, localPath, self.networkId):
            print "find new tab!"
            self.totalNew += 1
            return False
        else:
            return True
    
    def finish(self):
        print "抓取完毕，此次总共新增谱 %d个"%(self.totalNew)
        self.db.close()
        
    def setNetwork(self,networkId):
        self.networkId = networkId
        
    def start(self):
        pass
