from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from predict.prediction import get_prediction
from PIL import Image

myapp = Flask(__name__)


@myapp.route('/')
def hello():
    return render_template('index.html')

@myapp.route('/submit', methods=['POST'])
def predict():
    try:
        if request.method == "POST":
            file = request.files['file']
            # print(file)
            file.save("./static/images/" + secure_filename(file.filename))
            # file.save("./static/images/img" + secure_filename(file.filename).split(".")[1])
            # save_path = "./static/images/img" + secure_filename(file.filename).split(".")[1]
            save_path = "./static/images/" + secure_filename(file.filename)
            image = Image.open(save_path)
            class_id, class_name = get_prediction(image=image)
            print(class_id, "abc")
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
    myapp.run()