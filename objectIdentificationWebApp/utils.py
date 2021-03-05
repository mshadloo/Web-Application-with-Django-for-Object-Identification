import pickle
def load_images(file_Name):

    pkl_file = open(file_Name, 'rb')
    f = pickle.load(pkl_file)
    images= f['images']
    img_names = f['img_names']

    pkl_file.close()
    return images,img_names
def save_image_features(images, img_names,fileName):
    f = {}
    f['images'] = images
    f['img_names'] = img_names
    fName = open(fileName, "wb")
    pickle.dump(f, fName)
    fName.close()
