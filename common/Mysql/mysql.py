import pymysql

#class MyDB:

class MySQL():


    '''检测数据库数据'''
    def Mysql(mysqltext):
        # 打开数据库连接
        db = pymysql.connect("10.0.201.234","root","yk1234","parking")
        # 使用cursor()方法创建一个游标对象
        cursor =db.cursor()
        # 使用execute()方法执行sql查询
        cursor.execute(mysqltext)

        # 使用fetchone()方法获取单条数据
        data = cursor.fetchone()
        # dataall = cursor.fetchall()

        print("查到的数据：",data)
        if data != None:
            print("查到数据，用例成功")
        else:
            print("没有查到数据，用例失败")
            raise
        # print("database all ",dataall)

        # print("row count ",self.cursor.rowcount)
        # 关闭数据库连接
        cursor.close()


    '''检测被删除的数据库数据'''
    def Mysql_delete(mysqltext):
         # 打开数据库连接
        db = pymysql.connect("10.0.201.234","root","yk1234","parking")
        # 使用cursor()方法创建一个游标对象
        cursor =db.cursor()
        # 使用execute()方法执行sql查询
        cursor.execute(mysqltext)

        # 使用fetchone()方法获取单条数据
        data = cursor.fetchone()
        # dataall = cursor.fetchall()

        print("查到的数据：",data)
        if data != None:
            print("查到数据，用例失败")
            raise
        else:
            print("没有查到数据，用例成功")
        # print("database all ",dataall)

        # print("row count ",self.cursor.rowcount)
        # 关闭数据库连接
        cursor.close()

    '''检测数据库多条数据'''
    def Mysql_two(mysqltext,mysqltext_two,number):
        # 打开数据库连接
        db = pymysql.connect("10.0.201.234","root","yk1234","parking")
        # 使用cursor()方法创建一个游标对象
        cursor =db.cursor()
        # 使用execute()方法执行sql查询
        cursor.execute(mysqltext)

        # 使用fetchone()方法获取单条数据
        data = cursor.fetchone()
        # dataall = cursor.fetchall()

        print("查到的数据：",data)
        if data != None:
            print("查到数据，开始查询下一条数据")
            cursor.execute(mysqltext_two)
            data1 = cursor.fetchone()
            print("查到的第二条数据的值：",data1)
            if number in data1:
                print("两条数据都查到，用例成功")
            else:
                print("没有查到第二条数据，用例失败")
                raise
        else:
            print("没有查到数据，用例失败")
            raise
        # print("database all ",dataall)

        # print("row count ",self.cursor.rowcount)
        # 关闭数据库连接
        cursor.close()

    '''删除数据库表内容'''
    def Mysql_delete_tables(text):
        # 打开数据库连接
        db = pymysql.connect("10.0.201.234","root","yk1234","parking")
        # 使用cursor()方法创建一个游标对象
        cursor =db.cursor()
        # 使用execute()方法执行sql删除语句
        cursor.execute(text)
        # 提交修改
        db.commit()
        print("数据已删除")
        # print("row count ",self.cursor.rowcount)
        # 关闭数据库连接
        cursor.close()
