# -*- coding: gbk -*- 
'''
Created on 2010-10-12
吉他谱
@author: cg
'''

from BaseGripper import *

DOWNLOAD = False;

class JitapuGripper(BaseGripper):
    def __init__(self):
        BaseGripper.__init__(self)
        self.setNetwork(1)
        self.BASEURL = "http://www.jitapu.com/"
        
    def start(self):
        for i in range(0,26):
            self.gripPersonList(chr(ord('Z')-i))
        self.gripPersonList("[0-9]")
        self.finish()
    
    def gripPersonList(self,param):
        page = self.gripper.getPageInfo("http://www.jitapu.com/listArtist.aspx?path=%s"%param)
        list1= Tools.getFromPatten('<td class="dlList1">(.*?)</td>', page, False)
        list2 = Tools.getFromPatten('<td class="dlAlter1">(.*?)</td>', page, False)
        list = list1 + list2;
        urls = Tools.getFromPatten("<a href='(.*?)&amp", list, False, True)
        for url in urls:
            try:
                songListUrl = self.BASEURL+url
                self.gripSongList(songListUrl)
            except Exception,e:
                print e 
    
    def gripSongList(self,url):
        page = self.gripper.getPageInfo(url)
        pairs = Tools.getFromPatten2("<span>&bull;</span><a href='(.*?)'>(.*?)</a>", page)
        for pair in pairs:
            title = str(pair[1])
            pageUrl = str(pair[0])
            title=title.replace("\t","")
            title=title.replace("\r","")
            title=title.replace("\n","")
            title=title.replace(" ","")
            pageUrl=pageUrl.replace("&amp;","&")
            pageUrl=(self.BASEURL+pageUrl).strip();
            self.gripSong(pageUrl)
            #print title + "--" + pageUrl

    def gripSong(self,url):
        page = self.gripper.getPageInfo(url)
        author=Tools.getFromPatten('歌手<strong>(.*?)</strong>', page, True).strip()       
        title=Tools.getFromPatten('<h3>(.*?)</h3>', page, True).strip()
        
        zone=Tools.getFromPatten('<div id="tab">(.*?)</iframe>', page, True)
        
        type=0;
        if re.match('.*<div id="imgTab">.*',zone):
            type= TAB_TYPE['IMAGE']
            imgAddr = Tools.getFromPatten('<img src="../../(.*?)"', zone, True)
            imgUrl = self.BASEURL+imgAddr
            localPath = "c:/tab/image/%s-%s.gif"%(author,title)
            if DOWNLOAD:
                Tools.downloadFile(imgUrl, localPath)
            #print "图片URL="+imgUrl
        elif re.match('.*<div id="txt">.*',zone):
            type= TAB_TYPE['TXT']
            txt = Tools.getFromPatten("<pre>(.*?)</pre>", zone, True)
            localPath = "c:/tab/txt/%s-%s.txt"%(author,title)
            if DOWNLOAD:
                Tools.writeFile(txt, localPath)
            #print "TXT谱 =" + txt
        elif re.match('.*<div id="gtp">.*',zone):
            type= TAB_TYPE['GTP']
            gtpAddr = Tools.getFromPatten("<form action='../..(.*?)'", zone, True)
            gtpUrl = self.BASEURL+gtpAddr
            localPath = "c:/tab/gtp/%s-%s.rar"%(author,title)
            if DOWNLOAD:
                Tools.downloadFile(gtpUrl, localPath)
            #print "GTP谱url="+ gtpUrl
        
        self.findTab(author, title, type, url, localPath)


        #print zone
if __name__ == '__main__': 
    gripper = JitapuGripper();
    gripper.start()
    #gripper.gripSongList('http://www.jitapu.com/listSong.aspx?id=609')
    #gripper.gripSong('http://www.jitapu.com/CreatHtml.aspx?id=4452&creat=False&class=2&Url=579/gtp20051529101543.htm')
    #gripper.gripSong('http://www.jitapu.com/tabPages/4996/txt20104925014914.htm')
    #gripper.gripSong('http://www.jitapu.com/tabPages/609/gtp20075002025013.htm')
    
    