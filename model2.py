

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import keras
import cv2
import os

import numpy as np
import cv2 as cv
import PIL

import serial
import numpy as np




class Model:

    def __init__(self):
        #self.model = keras.models.load_model("C:/Users/hharun2/OneDrive - University of Nebraska-Lincoln/Desktop/Desktop/Arduino/camera-classifier-master 1/saved model serialize/model 1")
        self.model = keras.models.load_model("C:/Users/hharun2/OneDrive - University of Nebraska-Lincoln/Desktop/Desktop/Arduino/camera-classifier-master 1/trycodes/Model1epoch")


    def action(self,s):
        with serial.Serial('COM5', 9600) as ser:
            x = ser.readline()
            print(x)


            str_1 = s
            #c=fix("B")
            str_1_encoded = bytes(s,'UTF-8')
            #str_1_encoded = bytes(c,'UTF-8')
            #ser.write( b'\x0101')
            ser.write(str_1_encoded)
            
            #y = ser.readline()
            #print(y)
            
            ser.close()


    def predict(self, frame):
        frame = frame[1]
        cv.imwrite("frame.png", cv.cvtColor(frame, cv.COLOR_BGR2RGB ))
        img = PIL.Image.open("frame.png")
        img.thumbnail((640, 480), PIL.Image.ANTIALIAS)
        img=img.resize((200, 200), PIL.Image.ANTIALIAS)
        img.save("frame.png")

        x = image.img_to_array(img)
        x = np.expand_dims(x,axis = 0)
        images = np.vstack([x])
        val = self.model.predict(images)
        
        return np.argmax(val[0])


    

      
        
        
        
        
        
    


