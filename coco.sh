wget http://images.cocodataset.org/zips/val2014.zip
unzip val2014.zip 
rm val2014.zip
mv val2014 coco
mv coco  ./objectIdentificationWebApp/static
cd objectIdentificationWebApp
python coco_featureExtraction.py
