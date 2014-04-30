# -*- coding: gbk -*- 

from Tools import *
import MySQLdb
import time

DBCHARSET = "gbk"

'''''  
���ݿ�������  
'''  
class DBAdapter(object):   
       
    def __init__(self):   
        self.param = {'ip':'',   
                      'port':0,   
                      'user':'',   
                      'pw':'',   
                      'db':''}   
        self.connect_once = False  #�Ƿ����ӹ����ݿ�   
       
    '''''  
            ����/�������ݿ����ӳ�  
    '''  
    def connect(self,ip,port,user,pw,db):   
        if( ip != self.param['ip'] or  
            port != self.param['port'] or  
            user != self.param['user'] or  
            pw != self.param['pw'] or  
            db != self.param['db']):   
            try:   
                if self.connect_once == True: #�ͷ��ϴ�����  
                    try: 
                        self.cur.close()   
                        self.conn.close()
                    except:
                        Tools.writelog("���ݿ�رճ���")   
                self.conn=MySQLdb.connect(user=user,passwd=pw,db=db,host=ip,port=int(port))   
                self.conn.set_character_set(DBCHARSET)   
                self.connect_once = True  
                self.cur=self.conn.cursor(MySQLdb.cursors.Cursor)   
                self.param['ip'] = ip   
                self.param['port'] = port   
                self.param['user'] = user   
                self.param['pw'] = pw   
                self.param['db'] = db   
            except:     
                raise  
    '''''  
            ִ��SQL���  
    '''  
    def execute(self,sql):   
        try:   
            self.cur.execute(sql)   
        except:     
            raise  
    
    '''
          ��ȫsql
    '''               
    def sqlSafe(self,str):
        return str.replace("'","''")               
    
    '''''  
            ��ѯ���ݿ�  
    '''  
    def query(self,sql):   
        row = {}   
        self.execute(sql)   
        row=self.cur.fetchall()   
        return row
    
    '''
    �ر�����
    '''
    def close(self):
        self.cur.close()   
        self.conn.close() 
    
if __name__ == '__main__':
    db = DBAdapter()
    db.connect("127.0.0.1", 3306, "root", "KOFcgwin", "tabs")

    #db.execute("insert into tab values(null,'','',1,'',1,'',null,null)")
    db.updateTab("earth angel", "Ѻβ��̫��", 3, "http://www.jitapu.com/CreatHtml.aspx?id=24096&creat=False&class=2&Url=4992/gtp20104007044024.htm", "test", 1)