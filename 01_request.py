from flask import Flask,request

app=Flask(__name__)


# 127.0.0.1:5000/index?city=shenzhen &country=china  查询字符串 QueryString
@app.route("/index",methods=["GET","POST"])
def index():
    # request 中包含了前端发送过来的所有请求数据
    # form 和 data是用来提取请求体数据
    # 通过request.form 可以直接提取请求体中的表格格式数据，是一个类字典的对象
    name=request.form.get("name")
    age=request.form.get("age")
    city=request.args.get("city")
    print("request.data:%s" % request.data)
    return "hello name=%s ,age=%s,city=%s" % (name,age,city)


if __name__=='__main__':
    app.run(debug=True)
