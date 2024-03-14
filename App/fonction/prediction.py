from tensorflow.keras.models import load_model
import cv2
import numpy as np
import os 

IMG_HEIGHT = 64
IMG_WIDTH = 64
IMG_CHANNELS = 3

PATH="App/fonction/my_model.h5"

li=["Pizza","Glace","Pâtes"]	

def predi(img):
    img=cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite("1.png", img)
    img=cv2.resize(img,[IMG_HEIGHT,IMG_WIDTH])
    img=img.reshape([1,IMG_HEIGHT,IMG_WIDTH,IMG_CHANNELS])
    print(os.listdir())
    model=load_model(PATH)
    pred=model.predict(img)
  
    liste=list(pred[0,:])
    print(liste)
    return li[liste.index(max(liste))]
