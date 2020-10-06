from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField
from wtforms.validators import DataRuquired,EqualTo

app=Flask(__name__)
#创建Manager管理类对象

# 定义表单的模型类
class RegisterForm(FlaskForm):
    """自定义注册表单模型类"""
    user_name=StringField(label=u"用户名",validators=[DataRuquired(u"用户名不能为空")])
    password=PasswordField(label=u"密码",validators=[DataRuquired(u"密码不能为空")])
    password2=PasswordField(label=u"确认密码",validators=[DataRuquired(u"确认密码不能为空"),EqualTo("password",u"两次密码不一致")])



@app.route("/register")
def register():
    #创建表单对象
    form=RegisterForm()
    return render_template("register.html",form=form)


if __name__ == "__main__":
    # app.run(debug=True)
    # 通过管理对象来启动flask
    app.run()