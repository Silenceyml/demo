from flask import Flask,render_template,request,redirect,session
from flask_cors import *
import json
app = Flask(__name__,static_url_path='/static',template_folder='templates')
app.secret_key = "sdsfdsgdfgdfgfh"
CORS(app, supports_credentials=True)

@app.route('/')
def root():
    if request.path == "/login":
        return None
    if not session.get("user_info"):
        return redirect("/login")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("userpwd")
        if username=="admin" and password=="pwd":
            session["user_info"] = username
            # session.pop("user_info")  #删除session
            return redirect("/index")
        else:
            # return render_template("login.html",**{"msg":"用户名或密码错误"})
            return render_template("login.html",msg="用户名或者密码错误")
    if request.method == "GET":
        return render_template('login.html')

@app.route("/index",methods=["GET","POST"])
def index():
    # if not session.get("user_info"):
    #     return redirect("/login")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True);