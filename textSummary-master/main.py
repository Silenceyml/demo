from flask import Flask,render_template,request,redirect,session,jsonify
from flask_cors import *
import os
import json
from textsummary import TextSummary
app = Flask(__name__,static_url_path='/static',template_folder='templates')
app.secret_key = "sdsfdsgdfgdfgfh"
CORS(app, supports_credentials=True)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))

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

# 用于测试上传，稍后用到
@app.route('/upload')
def upload_test():
    return render_template('upload.html')


# 上传文件
@app.route('/api/upload', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    # f = request.files['myfile']  # 从表单的file字段获取文件，myfile为该表单的name值

    if request.method == "POST":
        file = request.files['fileToUpload']
        #  file_name = "test.csv"
    file_name = file.filename
    file.save(os.path.join(file_dir, file_name))
    return jsonify({"errno": 0, "errmsg": "上传成功"})

@app.route('/CalcSummary/', methods=['GET', 'POST'])
def CalcSummary():
    data = request.data
    data = data.decode(encoding="utf-8")
    content = json.loads(data)
    text = content['text']
    title = content['title']
    textsummary = TextSummary()
    textsummary.SetText(title, text)
    summary = textsummary.CalcSummary()
    print(summary)
    return json.dumps(summary)


if __name__ == '__main__':
    app.run(debug=True);