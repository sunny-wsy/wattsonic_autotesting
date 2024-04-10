# encoding='utf-8'
import pymysql,sys
class Postsql(object):
    def __init__(self):
        #连接数据库
        try:
            # self.con = psycopg2.connect(database='dbpe_pre_release', user='maxtropy',
            #                             password='maxtropy', host='pgm-uf6o54h38924i3nu117890.pg.rds.aliyuncs.com', port=1921)
            #测试环境
            self.con = pymysql.connect(database='monitor', user='wattsonic',
                                        password='wattsonicqw12QW!@', host='outer-wattsonic.mysql.rds.aliyuncs.com', port=3306)

            self.cur=self.con.cursor()
        except Exception as e:
            print('数据库连接失败')


    def find_one(self,sql):
        """
        查找返回结果中的第一条数据
        :param sql: mysql查询语句
        :return: 查询结果
        """
        # self.con.commit()  #更新数据库的链接以便获取最新数据
        self.cur.execute(sql)
        return self.cur.fetchone()

    def find_all(self,sql):
        """
        返回查询结果中的所有数据
        """
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_many(self,sql,num):
        """
        查询返回结果中指定数量的数据
        :param sql: 查询语句
        :return: 查询结果
        """
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchmany(num)

    def find_count(self,sql):
        """
        查找返回结果的数量
        """
        self.con.commit()
        res = self.cur.execute(sql)
        return res
    def delete(self,sql):
        self.cur.execute(sql)
        self.con.commit()


    def dis_connect(self):
        """
        关闭游标，断开连接
        """
        self.cur.close()
        self.con.close()
# class Postsql2(object):
#
#     def __init__(self):
#         #连接数据库
#         try:
#             # self.con = psycopg2.connect(database='dbpe_pre_release', user='maxtropy',
#             #                             password='maxtropy', host='pgm-uf6o54h38924i3nu117890.pg.rds.aliyuncs.com', port=1921)
#
#             self.con = psycopg2.connect(database='kingfisher', user='kingfisher',
#                                         password='AJoc0lmqhUrj', host='10.49.16.81', port=30432)
#             # self.con = psycopg2.connect(database='migrateTest', user='kingfisher-config',
#             #                             password='kingfisher-config', host='10.34.0.204', port=5432)
#
#             self.cur=self.con.cursor()
#         except Exception as e:
#             print('数据库连接失败')
#
#
#     def find_one(self,sql):
#         """
#         查找返回结果中的第一条数据
#         :param sql: mysql查询语句
#         :return: 查询结果
#         """
#         # self.con.commit()  #更新数据库的链接以便获取最新数据
#         self.cur.execute(sql)
#         return self.cur.fetchone()
#
#     def find_all(self,sql):
#         """
#         返回查询结果中的所有数据
#         """
#         self.con.commit()
#         self.cur.execute(sql)
#         return self.cur.fetchall()
#
#     def find_many(self,sql,num):
#         """
#         查询返回结果中指定数量的数据
#         :param sql: 查询语句
#         :return: 查询结果
#         """
#         self.con.commit()
#         self.cur.execute(sql)
#         return self.cur.fetchmany(num)
#
#     def find_count(self,sql):
#         """
#         查找返回结果的数量
#         """
#         self.con.commit()
#         res = self.cur.execute(sql)
#         return res
#     def delete(self,sql):
#         self.cur.execute(sql)
#         self.con.commit()
#
#
#     def dis_connect(self):
#         """
#         关闭游标，断开连接
#         """
#         self.cur.close()
#         self.con.close()

#
# sql="select * from t_bat limit10;"
# result=Postsql().find_one(sql)
# print (result)