from werkzeug.utils import secure_filename
from flask import Flask, render_template, jsonify, request
import os


app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))



# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


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

if __name__ == '__main__':
    app.run(debug=True)