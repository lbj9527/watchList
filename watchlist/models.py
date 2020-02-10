#模型类
from flask_login import UserMixin
from watchlist import db
from werkzeug.security import generate_password_hash, check_password_hash

#######################################################建立数据库操作函数#########################################################
#创建模型类
class User(db.Model, UserMixin):     #表名将会是user;继承UserMixin类会让 User 类拥有几个用于判断认证状态的属性和方法
    id = db.Column(db.Integer, primary_key=True)   #主键
    name = db.Column(db.String(20))                #名字
    username = db.Column(db.String(20))            #用户名
    password_hash = db.Column(db.String(128))      #密码散列值

    def set_password(self, password):      #用来设置密码的方法，接受密码作为参数
        self.password_hash = generate_password_hash(password)      #将生成的密码保存到对应字段     

    def validate_password(self, password):      #用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.password_hash, password)     #返回布尔值

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))    #电影标题
    year = db.Column(db.String(4))      #电影年份