#local
# from predict.prediction import get_prediction
# with open("./images/Domestic-feline-tabby-cat.jpg", 'rb') as f:
#     image_bytes = f.read()
#     print(get_prediction(image_bytes=image_bytes))
#flask
import requests

resp = requests.post("http://localhost:5000/submit",
                     files={"file": open('./images/Domestic-feline-tabby-cat.jpg','rb')})
# print(resp.json())