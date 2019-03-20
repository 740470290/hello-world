from flask import Flask, request, render_template, redirect, url_for
import time
from flask_sqlalchemy import SQLAlchemy
import sqlite3 as sql

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    con = sql.connect("mydb")
    cur = con.cursor()
    if request.method == 'POST':
        user = request.form.get('say_user')
        text = request.form.get('say_password')
        # date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        cur.execute("INSERT INTO students (name,password) VALUES(?, ?)",(user,text) )
        con.commit()
    cur.execute("select * from students")
    ulist = cur.fetchall()
    return render_template('index.html', says=ulist)
@app.route('/del/', methods=['GET', 'POST'])
def del_user():
    con = sql.connect("mydb")
    cur = con.cursor()
    # 根据摸个字段作删除,filter_by蕾仕于where条件限定
    # 翻译为：delete from user where id= 1
    if request.method == 'POST':
        userId = request.form.get('userId')
        cur.execute("delete from students where id=" + userId)
        cur.execute("update students set id=id-1 where id>" + userId)
        con.commit()
    # else:
    cur.execute("select * from students")
    ulist = cur.fetchall()
    return render_template('index.html', says=ulist)
@app.route('/edits/', methods=['GET', 'POST'])
def edit_user():
    con = sql.connect("mydb")
    cur = con.cursor()
    # 根据摸个字段作删除,filter_by蕾仕于where条件限定
    # 翻译为：delete from user where id= 1
    if request.method == 'POST':
        userId = request.form.get('userId')
        user = request.form.get('say_user')
        text = request.form.get('say_password')
        cur.execute("update students set name=" +"\'"+ user+"\'" + ", password =" +"\'"+ text +"\'"+ " where id=" + userId)
        con.commit()
    # else:
    cur.execute("select * from students")
    ulist = cur.fetchall()
    return render_template('index.html', says=ulist)

# 程序入口
if __name__ == '__main__':
    app.run(debug=True)
