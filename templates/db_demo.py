from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI="mysql://root:7515@127.0.0.1:3306/db_python04"
    #设置sqlalchemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS=True

app.config.from_object(Config)
#创建数据库sqlachemy工具对象
db=SQLAlchemy(app)


class Role(db.Model):
    """用户角色/身份表"""
    __tablename__="tbl_roles"

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(32),unique=True)

    users=db.relationship("User",backref="role")


class User(db.Model):
    """用户表"""
    __tablename__="tbl_users"   #指明数据库的表明

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),unique=True)
    email=db.Column(db.String(128),unique=True)
    password=db.Column(db.String(128))
    role_id=db.Column(db.Integer,db.ForeignKey("tbl_roles.id"))




if __name__ == "__main__":
    # 清除数据库里的所有数据
    db.drop_all()

    #创建所有表
    db.create_all()
    
    #创建对象
    role1=Role(name="admin")
    # session 记录对象任务
    db.session.add(role1)
    # 提交任务到数据库中
    db.session.commit()

    role2=Role(name="stuff")
    db.session.add(role2)
    db.session.commit()

    us1=User(name='wang',email='wang@163.com',password='123456',role_id=role1.id)
    us2=User(name='zhang',email='wang@189.com',password='123456',role_id=role2.id)
    us3=User(name='chen',email='wang@126.com',password='123456',role_id=role1.id)
    us4=User(name='zhou',email='zhang@163.com',password='123456',role_id=role2.id)

    db.session.add_all([us1,us2,us3,us4])
    db.session.commit()

