# -*- coding: gbk -*- 
'''
Created on 2010-11-25
gtp中国

@author: cg
'''

from BaseGripper import *

class GtpCnGripper(BaseGripper):
    def __init__(self):
        BaseGripper.__init__(self)
        self.setNetwork(4)
        self.BASEURL = "http://www.gtp.cn/"
        self.PAGEBASEURL = "http://www.gtp.cn/gtp/htm/gtp_a10_more/"
        
    def start(self):
        currPage = self.PAGEBASEURL + "gtp_a1_1.htm"
        while self.gripPage(currPage) == False:
            if self.nextPage == "":
                break
            currPage = self.PAGEBASEURL + self.nextPage
        self.finish()
    
    def gripPage(self,url):
        print "gripping url=%s"%url
        page = self.gripper.getPageInfo(url)
        #page = Tools.toUnicode(page, "gb2312")
        tips = Tools.getFromPatten2('<TR align=left><TD width=185 height=24 style="BORDER-bottom: #999999 1px dotted">(.*?)</tr>',page)
        for tip in tips:
            title = Tools.getFromPatten("target=_blank>(.*?)</a>",tip,True)
            if re.match('.*<b>.*',title):
                title = Tools.getFromPatten("<b>(.*?)</b>",title,True)
            if title=="":
                continue
            zone = Tools.getFromPatten('<TD width="68"  height=24 style="BORDER-bottom: #999999 1px dotted">(.*?) </TD>',tip,True)
            artist = Tools.getFromPatten('>(.*?)</a>',zone,True)
            type=TAB_TYPE['GTP']
            ref_url = Tools.getFromPatten('<a href=\.\./\.\./\.\./(.*?)  target=_blank>',tip)
            ref_url = self.BASEURL + ref_url
            
            if self.findTab(artist, title, type, ref_url, ""):
                return True #找到相同的，不再继续了
        
        #get next page
        zone = Tools.getFromPatten('<table border="0" width="100%" cellspacing="0"   cellpadding="0">(.*?)</table>',page,True)
        links = Tools.getFromPatten2('<a href=(.*?)>',zone)
        self.nextPage = ""
        for link in links:
            if re.match(".*下一页.*",link):
                self.nextPage = link.replace('title="下一页"','')

        return False

if __name__ == '__main__': 
    gripper = GtpCnGripper();
    gripper.start()
    #gripper.gripPage("http://www.gtp.cn/gtp/htm/gtp_a10_more/gtp_a1_1.htm")
    
    