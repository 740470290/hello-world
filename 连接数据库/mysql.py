import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="123456",
      database = 'runoob_db'
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM sites")

myresult = mycursor.fetchall()     # fetchall() 获取所有记录

for x in myresult:
  print(x)
--------------------------------------------------
import pymysql
#2.插入操作
db= pymysql.connect(host="localhost",user="root",
 	password="123456",db="mydb",port=3306)

# 使用cursor()方法获取操作游标
cur = db.cursor()

sql_insert ="insert into NAME (name) values('徐州灵匠科技公司')"

cur.execute(sql_insert)
db.commit()
---------------------------------------
import pymysql
import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',user='root',password='123456',db='测试网站连接.py',port=3306)

print("数据库连接成功")

cur = connection.cursor()

sql = 'select * from student'
sql1 = "INSERT INTO student(id,name,sex,years)VALUES(7,'ZHANG','girl',25)"
try:

    cur.execute(sql)
    # cur.execute(sql1)
    connection.commit()
    result = cur.fetchall()
    print("序号","姓名","性别","年龄")
    for row in result:

        id = row[0]
        name = row[1]
        sex = row[2]
        years = row[3]

        print(" ",id,name,sex,years)


finally:
    connection.close()
