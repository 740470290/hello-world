from flask import Flask, request, render_template, redirect, url_for
import time
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')
# 实例化一个数据库对象
db = SQLAlchemy(app)
# users = []  # 这里存放所有的留言
# 建立一个类来影射数据库表，将数据库的模型作为参数传入
class User(db.Model):
    # 声明表名
    _tablename_ = 'user'
    # 建立函数字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    password = db.Column(db.String(200))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        ulist = User.query.all()
        for i in ulist:
            print(i)
        return render_template('index.html', says=ulist)
    else:
        user = request.form.get('say_user')
        text = request.form.get('say_password')
        # date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        user = User(name=user, password=text)
        # 调用添加方法
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
@app.route('/del/', methods=['GET', 'POST'])
def del_user():
    # 根据摸个字段作删除,filter_by蕾仕于where条件限定
    # 翻译为：delete from user where id= 1
    if request.method == 'GET':
        ulist = User.query.all()
        return render_template('index.html', says=ulist)
    # else:
    userId = request.form.get('userId')
    User.query.filter_by(id=userId).delete()
    db.session.execute("alter table user drop id;")
    db.session.execute("alter table user add id int(5) not null primary key auto_increment first;")
    db.session.commit()
    return redirect(url_for('del_user'))
@app.route('/edits/', methods=['GET', 'POST'])
def edit_user():
    # 根据摸个字段作删除,filter_by蕾仕于where条件限定
    # 翻译为：delete from user where id= 1
    if request.method == 'GET':
        ulist = User.query.all()
        return render_template('index.html', says=ulist)
    # else:
    userId = request.form.get('userId')
    user = request.form.get('say_user')
    text = request.form.get('say_password')
    User.query.filter_by(id=userId).update({'name': user,'password': text})
    db.session.commit()
    return redirect(url_for('edit_user'))
# #指定数据库连接还有库名
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql@127.0.0.1:3306/myflask?charset=utf8'
# 制定配置，用来省略操作
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# # 数据库入库操作
# @app.route('/')
# def index():
#
#
#     # 增，入库逻辑
#     # 声明对象
#     user = User(name='哈哈', password='456456')
#     # 调用添加方法
#     db.session.add(user)
#     # #提交入库
#     db.session.commit()
#     return '这里是首业'
# # 数据库删除操作
# @app.route('/del')

#
#     return '这里是删除操作'
#
#
# # 数据库改操作（改）
# @app.route('/edit')
# def edit_user():
#
#
#     # 根据摸个字段做修改操作
#     # 翻译为 update user set name = '张三' where id = 8
#     User.query.filter_by(id=1).update({'password': '123456'})
#
#     # 使用原生语句进行修改操作
#     db.session.execute("update user set password = '123321' where id = 9")
#     return '这里是改操作'
#
#
# # 数据库的查询操作（查）
# @app.route('/select')
# def select_user():
#
#
#     # 简单的全量查询
#     ##翻译为：select * from user
#     ulist = User.query.all()
#     print(ulist)
#     for i in ulist:
#         print(i.name)
#     # 直取一条
#     ulist = User.query.first()
#     print(ulist)
#     # 使用原生的sql语句
#     # 翻译以为: select * from user order by desc limit 1,2
#     # items = db.session.execute('select * from user order by id desc limit 1,2')
#     items = db.session.execute('select * from user ')
#
#     # 将结果集强转为list
#     items = list(items)
#
#     return render_template('day5.html', items=items)

# 程序入口
if __name__ == '__main__':
    app.run(debug=True)
