from django.apps import AppConfig
import tensorflow.keras as K
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import pickle
import numpy as np
import os
def load_images(file_Name):

    pkl_file = open(file_Name, 'rb')
    f = pickle.load(pkl_file)
    images= f['images']
    img_names = f['img_names']

    pkl_file.close()
    return images,img_names

class ObjectidentificationConfig(AppConfig):
    name = 'objectIdentification'
    dataset = 'coco'
    data_dir = 'data'

    resnet = ResNet50(weights='imagenet')
    model = K.Model(inputs=resnet.input, outputs=resnet.layers[-2].output)
    IMG_SIZE = 224

    images, img_names = load_images(os.path.join(data_dir, dataset, "images.pkl"))

    def nearest_neighbors(img_path, k):
        img = image.load_img(img_path, target_size=(ObjectidentificationConfig.IMG_SIZE, ObjectidentificationConfig.IMG_SIZE))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        feature_x = ObjectidentificationConfig.model.predict(x)
        idx = np.argsort(np.sum((ObjectidentificationConfig.images - feature_x) ** 2, axis=1))
        nearest_img_names = []
        for i in idx[:k]:
            nearest_img_names.append(ObjectidentificationConfig.dataset + "/" + ObjectidentificationConfig.img_names[i])
        return nearest_img_names

    def image_classification(img_path):
        img = image.load_img(img_path, target_size=(ObjectidentificationConfig.IMG_SIZE, ObjectidentificationConfig.IMG_SIZE))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        preds = ObjectidentificationConfig.resnet.predict(x)
        predictions = decode_predictions(preds, top=3)[0]
        print('Predicted:', predictions)
        res = [(np.round(e[2] * 100, 2), e[1]) for e in predictions if np.round(e[2] * 100, 2) != 0]
        return res

