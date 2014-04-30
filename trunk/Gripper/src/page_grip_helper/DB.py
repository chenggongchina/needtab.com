# -*- coding: gbk -*- 

from Tools import *
import MySQLdb
import time

DBCHARSET = "gbk"

'''''  
数据库适配器  
'''  
class DBAdapter(object):   
       
    def __init__(self):   
        self.param = {'ip':'',   
                      'port':0,   
                      'user':'',   
                      'pw':'',   
                      'db':''}   
        self.connect_once = False  #是否连接过数据库   
       
    '''''  
            创建/更新数据库连接池  
    '''  
    def connect(self,ip,port,user,pw,db):   
        if( ip != self.param['ip'] or  
            port != self.param['port'] or  
            user != self.param['user'] or  
            pw != self.param['pw'] or  
            db != self.param['db']):   
            try:   
                if self.connect_once == True: #释放上次连接  
                    try: 
                        self.cur.close()   
                        self.conn.close()
                    except:
                        Tools.writelog("数据库关闭出错")   
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
            执行SQL语句  
    '''  
    def execute(self,sql):   
        try:   
            self.cur.execute(sql)   
        except:     
            raise  
    
    '''
          安全sql
    '''               
    def sqlSafe(self,str):
        return str.replace("'","''")               
    
    '''''  
            查询数据库  
    '''  
    def query(self,sql):   
        row = {}   
        self.execute(sql)   
        row=self.cur.fetchall()   
        return row
    
    '''
    关闭连接
    '''
    def close(self):
        self.cur.close()   
        self.conn.close() 
    
if __name__ == '__main__':
    db = DBAdapter()
    db.connect("127.0.0.1", 3306, "root", "KOFcgwin", "tabs")

    #db.execute("insert into tab values(null,'','',1,'',1,'',null,null)")
    db.updateTab("earth angel", "押尾光太郎", 3, "http://www.jitapu.com/CreatHtml.aspx?id=24096&creat=False&class=2&Url=4992/gtp20104007044024.htm", "test", 1)