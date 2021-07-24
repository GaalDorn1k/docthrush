import numpy as np 
from pdf2image import convert_from_path
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
#import wand as wd
import numpy as np
from PIL import Image
import glob
import os, sys, os.path, time
from tensorflow.keras import Input
from tensorflow.keras import Model
#from tensorflow.keras.utils import np_utils




def learning (x_train, y_train):
    #model = Sequential()
    #model.add(Dense(810*570*3, activation = 'relu', input_shape=(810*570*3,)))
    inp = Input(shape=(810*570*3,))
    #layer=Dense(8000, activation='relu')(inp)
    out = Dense(2,  activation = 'softmax')(inp)
    #model.add(Dense(2,  activation = 'softmax'))
    model=Model(inputs = inp, outputs = out)
    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs = 50)
    
    return model



#def learning (x_train, y_train):

  #  inp = Input(shape=(810*570*3,))
    #layer=Dense(8000, activation='relu')(inp)
  #  out = Dense(1,  activation = 'sigmoid')(inp)
   # model=Model(inputs = inp, outputs = out)
   # model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
   # model.fit(x_train, y_train, epochs = 200)
    
    #return model


def usenet(path,model):
    os.chdir(path)
    rename0(path)
    i = sum([len(files) for r, d, files in os.walk(path)])
    pdf_to_png(path)
    resizeZ(path)
    data = png_to_list(path)
    data1 = np.array(data)
    data1.flatten()
    
#    print('asdsadsadsadsadsadsa ')
#    print(i)
    data1 = np.array(data1).reshape(i, 810*570*3)
   
    #data = np.array(data).reshape(29, 810*570*3)
    for file in os.listdir(path):
        if file.endswith(".png"):
           os.remove(file)
   
   
    pred= model.predict(data1)
    print (pred)

    for i in range(len(pred)):
        if pred[i] < 0.5:
            pred[i] = 0
        else:
            pred[i] = 1
    
    return pred


#path = "/root/Desktop/python/images/"
#dirs = os.listdir( path )

def resize(path):
    os.chdir(path)
    dirs = os.listdir( path )
    for item in dirs:
        if item.endswith(".png"):
            im = Image.open(item)
            f = os.path.splitext(item)
            imResize = im.resize((570,810), Image.ANTIALIAS)
            imResize.save(str(f) + ' resized.png', 'png', quality=90)




def resizeZ(path):
    os.chdir(path)
    dirs = os.listdir( path )
    for item in dirs:
        if item.endswith(".png"):
            im = Image.open(item)
            f = os.path.splitext(item)
            im = im.resize((570,810), Image.ANTIALIAS)
            im.save(item, quality=90)




def png_to_list(path):
    os.chdir(path)
    img = []
    for file in os.listdir(path):

        if file.endswith(".png"):
            
            im = np.array(Image.open(file))
               
            img.append(im)
             
    return img


def pdf_to_png(path):
    os.chdir(path)
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            images = convert_from_path(file, 70, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
            #for i, image in enumerate(images):
            fname = file +'.png'
            images[0].save(fname, "PNG")
        
        
    for file in os.listdir(path):
        if file.endswith(".PDF"):
            images = convert_from_path(file, 70,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
            #for i, image in enumerate(images):
            fname = file +'.png'
            images[0].save(fname, "PNG")



def rename0(path):
    os.chdir(path)
    i = 0
    for file in os.listdir(path):
        os.rename(file, str(i) + '.pdf')
        i+=1


def rename(path, pred, name0, name1):
    os.chdir(path)
    pred = np.array(pred)
    pred.flatten()
    print(pred)
    i = 0
    j=0
    k=0
    for file in os.listdir(path):
        if pred[i] == 1: 
            os.rename(file, str(name0) + str(j) + '.pdf')
            j+=1
        else:
            os.rename(file, str(name1) + str(k) + '.pdf')
            k+=1
        i+=1