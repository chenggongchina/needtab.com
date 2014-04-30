# -*- coding: gbk -*- 
'''
Created on 2010-10-12

@author: cg
'''
import socket
import urllib2

'''''  
网页内容爬虫  
'''  
class PageGripper():   
    URL_OPEN_TIMEOUT = 15 #网页超时时间   
    MAX_RETRY = 3 #最大重试次数   
       
    def __init__(self):   
        socket.setdefaulttimeout(self.URL_OPEN_TIMEOUT)    
       
    #尝试获取页面   
    def downloadUrl(self,url):   
        charset = ""   
        page = ""   
        retry = 0  
        while True:   
            try:   
                fp = urllib2.urlopen(url)   
                break  
            except urllib2.HTTPError: #状态错误    
                raise urllib2.HTTPError   
            except urllib2.URLError: #网络错误超时   
                retry+=1  
                if( retry > self.MAX_RETRY ):    
                    raise urllib2.URLError   
       
        while True:   
            line = fp.readline()   
            page += line
            if not line:   
                break  
        fp.close()   
        return page   
       
    #获取页面   
    def getPageInfo(self,url):    
        info = ""   
        try:   
            info = self.downloadUrl(url)   
        except Exception,e:   
            print "grip page TIME OUT"
        return info