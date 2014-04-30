# -*- coding: gbk -*- 
'''
Created on 2010-11-25
虫虫吉他

@author: cg
'''

from BaseGripper import *

class CcjtGripper(BaseGripper):
    def __init__(self):
        BaseGripper.__init__(self)
        self.setNetwork(2)
        self.BASEURL = "http://www.ccjt.net/"
        
    def start(self):
        nextPage = "pu_list.htm"
        while nextPage != "":
            nextPage = self.gripPage(self.BASEURL + nextPage)
        self.finish()
    
    def gripPage(self,url):
        print "gripping url=%s"%url
        page = self.gripper.getPageInfo(url)
        zone = Tools.getFromPatten2('<tbody id="(.*?)" >(.*?)</tbody>', page )
        for tip in zone:
            line = Tools.toUnicode(tip[1],"gbk")
            #print line
            c1 = Tools.getFromPatten('<td nowrap="nowrap" class="icon">(.*?)</td>', line, True )
            if c1 == "":
                continue
            #print c1
            artist = Tools.getFromPatten('<em>\[(.*?)\]</em>', line, True )
            ref_url = Tools.getFromPatten('<a href="(.*?)" target="_blank" >', line, True )
            title = Tools.getFromPatten('target="_blank" >(.*?) </a>', line, True )
            type_txt = Tools.getFromPatten('<font color=#BGTPBGTPBGTP>(.*?)</font>', line, True )
            if re.match('.*GTP.*',type_txt):
                type=TAB_TYPE['GTP']
            elif re.match(u'.*六线.*',type_txt):
                type=TAB_TYPE['IMAGE']
            else:
                type=TAB_TYPE['TXT']
            self.findTab(artist, title, type, ref_url, "")
        page_zone = Tools.getFromPatten('<div class="pages">(.*?)</div>', page, True )
        
        links = Tools.getFromPatten2('<a href="(.*?)"(.*?)>(.*?)</a>', page_zone )
        nexturl = ""
        for link in links:
            if link[2]=="下一页":
                nexturl = link[0]
        return nexturl
    

if __name__ == '__main__': 
    gripper = CcjtGripper();
    gripper.start()
    #gripper.gripPage("http://www.ccjt.net/pu_list_0_12_0_5_8.htm")
    
    