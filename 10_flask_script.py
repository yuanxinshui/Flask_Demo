from flask import Flask,render_template
from flask_script import Manager

app=Flask(__name__)
#创建Manager管理类对象
# manager=Manager(app)

@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
    # 通过管理对象来启动flask
    # manager.run()