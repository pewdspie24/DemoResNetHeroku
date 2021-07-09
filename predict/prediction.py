from .prepare_data import transform_image
import json
from .resnet import resnet101

model = resnet101(pretrained=True)
imagenet_idx = json.load(open("./predict/imagenet_class_index.json"))

model.eval()

def get_prediction(image):
    tensor = transform_image(image)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    idx = str(y_hat.item())
    return imagenet_idx[idx]