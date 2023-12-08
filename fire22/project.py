import numpy as np
import keras
from keras import backend as K
from keras.layers.core import Dense, Activation
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.models import Model
from keras.applications import imagenet_utils
import h5py
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau,History
#from sklearn.metrics import confusion_matrix
#for broken data stream error
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import itertools
#for broken data stream error
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
model = keras.models.load_model('raks_model14.h5')

def processimage(path) :
    
    from IPython.display import Image
    Image(filename='fire2.jpg', width=300,height=200) 

    preprocessed_image = prepare_image('fire2.jpg')
    # preprocessed_image = prepare_image(path)
    predictions = model.predict(preprocessed_image)
    # print("Fire :",str(predictions[0][0]*100)[:4] + "%"," |Not Fire:",str(predictions[0][1]*100)[:4]+"%")
    labels=(predictions>0.5).astype(np.int)
    #print(labels)
    if labels[0][0]==1  :
        return "heat"
    else:
        return "no heat"



def prepare_image(file):
    img_path = ''
    # img=np.reshape(file, (224,224))
    img = keras.utils.load_img(img_path+ file, target_size=(224, 224))
    img_array = keras.utils.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims) 

# processimage()



# preprocessed_image = prepare_image('14.jpg')
# predictions = model.predict(preprocessed_image)
# print("Fire :",str(predictions[0][0]*100)[:4] + "%"," |Not Fire:",str(predictions[0][1]*100)[:4]+"%")
# labels=(predictions>0.5).astype(np.int)
# #print(labels)
# if labels[0][0]==1 :
#     print("Fire detected")
# else:
#     print("No Fire detected")