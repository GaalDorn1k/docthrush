import functions as fc
from tensorflow import keras
from tensorflow.keras import Model
from tensorflow.keras.models import load_model
#from keras.utils import np_utils
import numpy as np

#i = sum([len(files) for r, d, files in os.walk('C:\\Users\\admin\\Desktop\\Parser\\post')])

#j = sum([len(files) for r, d, files in os.walk('C:\\Users\\admin\\Desktop\\Parser\\rasp')])


path1 = 'C:\\Users\\admin\\Desktop\\Parser\\post'
path2 = 'C:\\Users\\admin\\Desktop\\Parser\\rasp'
  

fc.pdf_to_png(path1)
data1 = fc.png_to_list(path1)
fc.resizeZ(path1)


fc.pdf_to_png(path2)
fc.resizeZ(path2)
data2 = fc.png_to_list(path2)


data1 += data2
print(len(data1))
target=[]
ttarget=[]
for i in range (16):
    target.append(1)
for i in range (16):
    target.append(0)

i=0
for i in range(len(target)):
  if target[i]==0:
    ttarget.append([1,0])
  elif target[i]==1:
    ttarget.append([0,1])

print(ttarget)

data = np.array(data1)
tar = np.array(ttarget)
#print(tar)

data.flatten()
#print(data)
i=0
j=0
data=data.astype('float32')
data = data / 255




print(data)
data = np.array(data).reshape(32, 810*570*3)
#print(data[1][2].shape)
#for i in range(len(data)):
  #  data[i] = np.array(data[i]).reshape(810, 570)

model = Model()
model = fc.learning(data, tar)

model.save('model12.h5')