from flask import Flask,render_template,request,redirect,session
app = Flask(__name__,template_folder='templates')
app.secret_key = "sdsfdsgdfgdfgfh"

@app.route("/")
def root():
    if request.path=="/login":
        return None
    if not session.get("user_info"):
        return redirect("/login")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        # print(request.values)   #这个里面什么都有，相当于body
        username = request.form.get("username")
        password = request.form.get("password")
        if username=="haiyan" and password=="123":
            session["user_info"] = username
            # session.pop("user_info")  #删除session
            return redirect("/index")
        else:
            # return render_template("login.html",**{"msg":"用户名或密码错误"})
            return render_template("login.html",msg="用户名或者密码错误")


@app.route("/index",methods=["GET","POST"])
def index():
    # if not session.get("user_info"):
    #     return redirect("/login")
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)