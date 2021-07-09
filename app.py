from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField
from flask_wtf import FlaskForm
from predict.prediction import get_prediction
from PIL import Image
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])

def predict():
    try:
        if request.method == "POST":
            file = request.files['file']
            print(file)
            file.save("./static/images/" + secure_filename(file.filename))
            save_path = "./static/images/" + secure_filename(file.filename)
            image = Image.open(save_path)
            class_id, class_name = get_prediction(image=image)
            # return jsonify({'class_id': class_id, 'class_name': class_name})
            return render_template('index.html',message = class_name, user_image=save_path)
    except:
        return render_template('index.html',message = "failed")

# @app.route("/upload", methods = ['POST','GET'] )
# def up():
#     if request.method == 'POST':
#         print('POSTING')
#         print(request.files['photo'])
#         image = request.files['photo']
#         image.save('./images/img.jpg')
        
#         return render_template('index.html',user_image = 'static/Images/img.jpg')
#     else:
#         return render_template('index.html')

if __name__ == '__main__':
    app.run()