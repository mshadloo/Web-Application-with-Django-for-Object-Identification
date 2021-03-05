from django.db import models
from .apps import ObjectidentificationConfig
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
from config import args
# Create your models here.
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
IMG_SIZE = args["img_size"]
def nearest_neighbors(img_path, k):
    img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    feature_x = ObjectidentificationConfig.feature_model.predict(x)
    idx = np.argsort(np.sum((ObjectidentificationConfig.images - feature_x) ** 2, axis=1))
    nearest_img_names = []
    for i in idx[:k]:
        nearest_img_names.append(args["dataset"]+ "/" + ObjectidentificationConfig.img_names[i])
    return nearest_img_names

def image_classification(img_path):
    img = image.load_img(img_path,
                         target_size=(IMG_SIZE, IMG_SIZE))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = ObjectidentificationConfig.resnet.predict(x)
    predictions = decode_predictions(preds, top=3)[0]
    print('Predicted:', predictions)
    res = [(np.round(e[2] * 100, 2), e[1]) for e in predictions if np.round(e[2] * 100, 2) != 0]
    return res