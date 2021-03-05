from tensorflow.keras.applications.resnet50 import ResNet50
import tensorflow.keras as K
resnet = ResNet50(weights='imagenet')
args ={"resnet":resnet,"feature_model" :K.Model(inputs=resnet.input, outputs=resnet.layers[-2].output),"img_size":224,
       "dataset" : 'coco',"data_dir" :'data','static_dir':'static',"batch_size":512, "feature_file":"images.pkl"}
