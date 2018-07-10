from pymysql import connect,cursors
import configparser as cparser
from pymysql.err import OperationalError
import os
base_dir=os.path.dirname(os.path.dirname(__file__))
file_path=base_dir+"/db_config.ini"
cf=cparser.ConfigParser()
cf.read(file_path)
host=cf.get("mysqlconf","host")
port=cf.get("mysqlconf","port")
user=cf.get("mysqlconf","user")
password=cf.get("mysqlconf","password")
db_name=cf.get("mysqlconf","db_name")

# print(host,port,user,password,db_name)
class DB():
    def __init__(self):
        try:
            self.conn=connect(host=host,
                         user=user,
                         password=password,
                         db=db_name,
                         charset='utf8',
                         cursorclass=cursors.DictCursor)
        except OperationalError as e:
            print("mysql 错误%d：%s"%(e.args[0],e.args[1]))
    def clear(self,table_name,type):
        sql="delete from "+table_name+" where type='"+type+"'"
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
        self.conn.commit()
    def close(self):
        self.conn.close()
    #将tranlog表里的所有记录的接单状态改为success
    def update(self,type):
        sql="update fosordertranslog set third_sure_respose='success' where type='"+type+"'"
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
        self.conn.commit()

if __name__=="__main__":
    db=DB()
    #db.clear("fosordertranslog","美团")
    db.update("美团")
    db.close()