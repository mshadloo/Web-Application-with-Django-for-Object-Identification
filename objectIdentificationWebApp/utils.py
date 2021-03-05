import pickle
def load_images(file_Name):

    pkl_file = open(file_Name, 'rb')
    f = pickle.load(pkl_file)
    images= f['images']
    img_names = f['img_names']

    pkl_file.close()
    return images,img_names