# -*- coding: gbk -*- 
'''
Created on 2010-11-25
52吉他

@author: cg
'''

from BaseGripper import *

class WoaiGuitarGripper(BaseGripper):
    def __init__(self):
        BaseGripper.__init__(self)
        self.setNetwork(3)
        self.BASEURL = "http://www.52jt.net/singer-all.asp?/"
        
    def start(self):
        for id in range(1,6000):
            self.gripPage("%s%d.html"%(self.BASEURL,id),True)
        self.finish()
    
    def gripPage(self,url,isGripOtherPage=False):
        print "gripping url=%s"%url
        try:
            page = self.gripper.getPageInfo(url)
            page = Tools.toUnicode(page, "utf8")
        except:
            return
        
        self.getTabs(page)
        
        #爬其他分页
        if isGripOtherPage:
            zone = Tools.getFromPatten('<div align="right" style="width:710px; float:right;">(.*?)</div>',page,True)
            links = Tools.getFromPatten2("<a href='(.*?)' class='graya12'>(.*?)</a>",zone)
            for link in links:
                self.gripPage(link[0],False)
        return

    def getTabs(self,page):
        tips = Tools.getFromPatten2('<div id="gtp_detail">(.*?)<span style="width:40px; float:left;">',page)
        for tip in tips:
            title = Tools.getFromPatten(u'吉他谱">(.*?)</a>',tip,True)
            if title=="":
                continue
            artist = Tools.getFromPatten('<span style="width:100px; float:left;">(.*?)</span>',tip,True)
            if re.match('.*icon_gtp.*',tip):
                type=TAB_TYPE['GTP']
            elif re.match(u'.*icon_pic.*',tip):
                type=TAB_TYPE['IMAGE']
            else:
                type=TAB_TYPE['TXT']
            ref_url = Tools.getFromPatten('<a href="(.*?)" class="graya12" target="_blank',tip,True)
            self.findTab(artist, title, type, ref_url, "")

if __name__ == '__main__': 
    gripper = WoaiGuitarGripper();
    gripper.start()
    #gripper.gripPage("http://www.ccjt.net/pu_list_0_12_0_5_8.htm")
    
    