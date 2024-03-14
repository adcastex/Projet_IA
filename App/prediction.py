from tensorflow.keras.models import load_model
import cv2
import numpy as np

IMG_HEIGHT = 64
IMG_WIDTH = 64
IMG_CHANNELS = 3

PATH="Model/my_model.h5"

li=["Pizza","glace","pates"]	

def predi(img):
    img=cv2.resize(img,[IMG_HEIGHT,IMG_WIDTH])
    img=img.reshape([1,IMG_HEIGHT,IMG_WIDTH,IMG_CHANNELS])

    model=load_model(PATH)
    pred=model.predict(img)
    print(pred.shape)
    liste=list(pred[0,:])
    return li[liste.index(max(liste))]
