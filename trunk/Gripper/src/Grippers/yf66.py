# -*- coding: gbk -*- 
'''
Created on 2010-11-25
yf66缘分吉他

@author: cg
'''

from BaseGripper import *

class Yf66Gripper(BaseGripper):
    def __init__(self):
        BaseGripper.__init__(self)
        self.setNetwork(5)
        self.BASEURL = "http://www.yf66.com"

        
    def start(self):
        currPage = self.BASEURL + "/music.aspx?id=6"
        while self.gripPage(currPage) == False:
            if self.nextPage == "":
                break
            currPage = self.BASEURL + self.nextPage
        self.finish()
    
    def gripPage(self,url):
        print "gripping url=%s"%url
        page = ""
        while page == "":
            page = self.gripper.getPageInfo(url)
        #page = Tools.toUnicode(page, "gb2312")
        tips = Tools.getFromPatten2('<li class="pu_title list_bg">(.*?)</li>',page)
        tips2 = Tools.getFromPatten2('<li class="pu_title">(.*?)</li>',page)
        
        for tip in tips + tips2:
            title = Tools.getFromPatten('target="_blank">(.*?)</a>',tip,True)
            if title=="":
                continue

            artist = Tools.getFromPatten('<u>\[(.*?)\]</u>',tip,True)
            type=TAB_TYPE['IMAGE']
            
            ref_url = Tools.getFromPatten('<a href=\'/(.*?)\' target="_blank">',tip,True)
            ref_url = self.BASEURL + "/" + ref_url
            
            if self.findTab(artist, title, type, ref_url, ""):
                return False #找到相同的，不再继续了，改成True
        #get next page
        nextpage = Tools.getFromPatten('<a id="pagelist_xiaye" href="(.*?)">.*</a>', page,True)
        self.nextPage = nextpage.replace("amp;","")
        return False

if __name__ == '__main__': 
    gripper = Yf66Gripper();
    gripper.start()
    #gripper.gripPage("http://www.yf66.com/music.aspx?id=6")
    
    