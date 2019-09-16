import os
os.environ['GLOG_minloglevel'] = '2'
import numpy as np
from sklearn.externals import joblib 
import cv2
from keras.preprocessing import image
from keras.applications.imagenet_utils import preprocess_input
from keras_preprocessing.image import ImageDataGenerator
from keras.models import load_model
import keras.backend as K
from time import time


vid_fol = 'C:/Users/Piyush/Desktop/Final/'
vid_name = '3a.mp4'

cap = cv2.VideoCapture(vid_fol + vid_name)
model_dir = 'C:/Users/Piyush/Desktop/Final/'

t = time()

K.clear_session()
custom_resnet_model = load_model(model_dir+'testfinal2.h5')  

model_load_time = time() - t
print('Model Load Time = ' + str(model_load_time))
#******************************************************************************

test_datagen = ImageDataGenerator(
                
                preprocessing_function=preprocess_input,
                rescale=1./255
               
                )


me=[]
se=[]
ret, _ = cap.read()
cap.set(0, 0)
res = []
t = time()
i=0
while ret:
	print("Frame No: ",i)
	ret, I = cap.read()
	if not ret:
	    break

	I = cv2.resize(I, (224, 224))

	img = np.reshape(I,[1,224,224,3])
	img = img.astype('float32')
	img_data = test_datagen.standardize(img)
	me.append(img_data.mean())
	se.append(img_data.std())

	f_all = custom_resnet_model.predict(img_data)
	f_all = ["%.5f"%(100*f) for f in list(f_all[0])]
	res.append(f_all)
	i=i+1
run_time = time() - t
res = np.array(res)
np.save('predictions.npy', res, allow_pickle=False)
print('Model Load Time = ' + str(model_load_time))
print('Run Time = ' + str(run_time))
