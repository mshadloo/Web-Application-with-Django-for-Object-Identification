# Web Application with Django for Object Identification deployed in AWS Lightsail:
 ## To try web application you can go to http://34.220.204.100:8000/ 
 
 In this repo, I use Django to create web application and tensorflow as backend to do object identification.
 
 
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
