from flask import Flask,render_template,request,Response,redirect,flash
import os
from werkzeug.utils import secure_filename
import processing

f_path  = "static/uploads"
imgPath = 0

def save_file(obj):
    filename = 0
    for file in obj:
        filename = secure_filename(file.filename)  
        f_path1 = f_path
        f_path1 = os.path.join(f_path1, filename)
        if not os.path.exists(f_path1):
            file.save(f_path1)
    return filename


app = Flask(__name__)           
@app.route('/',methods=["get","post"])
def server_app():
    global imgPath
    if request.method=="GET":
        return render_template("dashboard.html")
    else:
        x = processing.decrypt_image(imgPath)
        x = "static/uploads/"+x
        return {"data":x}
@app.route('/form',methods=["get","post"])
def form():
    global imgPath
    try:
        if request.method == 'POST':
            img = request.files.getlist("image")
            im_name = save_file(img)
            imgPath = processing.encrypt_image(im_name)

    except Exception as e:
        print(e)
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)