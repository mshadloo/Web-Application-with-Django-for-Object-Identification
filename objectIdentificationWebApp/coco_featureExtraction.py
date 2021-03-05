from config import args
import os
import time
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np
from utils import save_image_features
images_dir = os.path.join(args["static_dir"],args["dataset"])
data_dir = os.path.join(args["data_dir"],args["dataset"])
if not os.path.exists(data_dir):
      os.makedirs(data_dir)
resnet = args["resnet"]
feature_model = args["feature_model"]
def load_images_from_directory(directory,image_size,batch_size=512):
    images = []
    img_names =[]
    batch = []
    i = 0
    for filename in os.listdir(directory):

        st = time.time()
        img_names.append(filename)
        img = image.load_img(os.path.join(directory, filename), target_size=image_size)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)

        x = preprocess_input(x)

        batch.append(np.squeeze(x))

        if len(batch) == batch_size:
            print('batch_No:', i)
            i += 1
            features = feature_model.predict(np.asarray(batch))
            batch = []
            images.extend(list(features))
            print('time', time.time() - st)
    if batch:
        features = feature_model.predict(np.asarray(batch))
        images.extend(list(features))

    return np.asarray(images),img_names
images,img_names = load_images_from_directory(images_dir,image_size=(args["img_size"], args["img_size"]))

save_image_features(images,img_names,os.path.join(data_dir,args["feature_file"]))
