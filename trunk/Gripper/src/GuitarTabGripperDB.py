# -*- coding: gbk -*- 

from page_grip_helper.DB import *

'''''  
�����������ݿ�������  
'''  
class GuitarGripperDBAdapter(DBAdapter):   
    
    '''
    �������׼�¼
    '''
    def updateTab(self,title,author,type,url,localPath,network):
        isNew = False;
        nowtime = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time())) 
        
        sql = "select * from tab where title='%s' and artist='%s' and network=%d and type=%d and ref_url='%s'"%(self.sqlSafe(title),self.sqlSafe(author),network,type,self.sqlSafe(url))
        exist = self.query(sql)
        if(len(exist)>=1):
            sql = "update tab set update_date='%s' where id=%s"%(nowtime,exist[0][0])
        else:
            isNew = True;
            sql = "insert into tab values(null,'%s','%s',%d,'%s',%d,'%s','%s','%s')"%(self.sqlSafe(title),self.sqlSafe(author),type,self.sqlSafe(url),network,self.sqlSafe(localPath),nowtime,nowtime)
        
        try:
            self.execute(sql)
        except Exception,e:
            print e   
        return isNew
    
if __name__ == '__main__':
    db = GuitarGripperDBAdapter()
    db.connect("127.0.0.1", 3306, "root", "KOFcgwin", "tabs")

    #db.execute("insert into tab values(null,'','',1,'',1,'',null,null)")
    db.updateTab("earth angel", "Ѻβ��̫��", 3, "http://www.jitapu.com/CreatHtml.aspx?id=24096&creat=False&class=2&Url=4992/gtp20104007044024.htm", "test", 1)