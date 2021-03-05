from django.apps import AppConfig
from config import args
from utils import load_images
import os


class ObjectidentificationConfig(AppConfig):
    name = 'objectIdentification'
    resnet = args["resnet"]
    feature_model = args["feature_model"]
    images, img_names = load_images(os.path.join(args["data_dir"], args["dataset"], "images.pkl"))



