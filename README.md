# Web Application with Django for Object Identification deployed in AWS Lightsail:
 ## To try this web application click [here](http://34.220.204.100:8000/) 
 
 In this repo, I use Django to create web application and tensorflow as backend to do object identification. I utilize Keras's ResNet50(pre-trained on ImageNet) to classify the given image. I also find ten most similar images among COCO-val2014 images to the given image. To achieve this, I load pretrained ResNet50 without fully connected layers and use it as feature extractor. I extract features from COCO-val2014 images using pretrained ResNet50 and store these features in numpy arrays. For the given image, I also extract features using pretrained ResNet50, and then b running K-neasret neighbor algorithm in Euclidean space, I find the most similar images to the given image.
 
 
 ### Project Requirements:
 The file [requirements.txt](https://github.com/mshadloo/Web-Application-with-Django-for-Object-Identification/blob/main/requirements.txt) contains all required packages to run the project.
 ### How to run:
```
git clone https://github.com/mshadloo/Web-Application-with-Django-for-Object-Identification.git
cd Web-Application-with-Django-for-Object-Identification
chmod +x run.sh && ./run.sh
```

 You also need to download [COCO dataset(2014 Val Images)](https://cocodataset.org/#download). To do so you can run the file [coco.sh](https://github.com/mshadloo/Web-Application-with-Django-for-Object-Identification/blob/main/coco.sh). 

After running [coco.sh](https://github.com/mshadloo/Web-Application-with-Django-for-Object-Identification/blob/main/coco.sh), move the folder "coco" to static folder of the project.
<br>
Run [coco_featureExtraction.py](https://github.com/mshadloo/Web-Application-with-Django-for-Object-Identification/blob/main/objectIdentificationWebApp/coco_featureExtraction.py) to extract features of COCO-Val2014 images using ResNet50 pretrained on ImageNet datset.
<br>
Now you can run web application using following command:

```console
python manage.py runserver
```
