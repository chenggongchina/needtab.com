# -*- coding: gbk -*- 
'''
Created on 2010-10-12

@author: cg
'''
import socket
import urllib2

'''''  
��ҳ��������  
'''  
class PageGripper():   
    URL_OPEN_TIMEOUT = 15 #��ҳ��ʱʱ��   
    MAX_RETRY = 3 #������Դ���   
       
    def __init__(self):   
        socket.setdefaulttimeout(self.URL_OPEN_TIMEOUT)    
       
    #���Ի�ȡҳ��   
    def downloadUrl(self,url):   
        charset = ""   
        page = ""   
        retry = 0  
        while True:   
            try:   
                fp = urllib2.urlopen(url)   
                break  
            except urllib2.HTTPError: #״̬����    
                raise urllib2.HTTPError   
            except urllib2.URLError: #�������ʱ   
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
       
    #��ȡҳ��   
    def getPageInfo(self,url):    
        info = ""   
        try:   
            info = self.downloadUrl(url)   
        except Exception,e:   
            print "grip page TIME OUT"
        return info