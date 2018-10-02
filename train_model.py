
# coding: utf-8

# In[32]:


from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.preprocessing.image import img_to_array
from keras.utils import np_utils
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse 
import imutils
import cv2
import os
from CNN.LeNet import LeNet


# In[33]:


#arser = argparse.ArgumentParser()
#arser.add_argrument("-d","--dataset",required=True,help ="the location path of dataset")
#arser.add_argrument("-m","--model",required=True,help="path to output model")
#rgs = vars(parser.parser_args())

data = []
labels = []
for it in sorted(list(paths.list_images("/home/cuong/Project/SmileOrNotSmile/dataset/SMILEs"))):
    img = cv2.imread(it)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = imutils.resize(img,width=28)
    img = img_to_array(img)
    data.append(img)
    
    label = it.split(os.path.sep)[-3]
    label = "smiling" if label == "positives" else "not_smiling"
    labels.append(label)


# In[34]:


#for it in labels:
#    print(it)


# In[35]:





# In[36]:


data = np.array(data,dtype="float")/255.0
labels = np.array(labels)

# In[37]:


le = LabelEncoder().fit(labels)


# In[38]:


labels = np_utils.to_categorical(le.transform(labels),2)
#labels


# In[39]:


classTotals = labels.sum(axis=0)
#classTotals


# In[40]:


classWeights = classTotals.max()/classTotals


# In[41]:


(trainX,testX,trainY,testY) = train_test_split(data,labels
                                              ,test_size=0.20,stratify=labels,random_state=42)


# In[42]:


#trainX


# In[45]:


print("compiling model ....")
model = LeNet.build(width=28, height=28, depth=1, classes=2)
model.compile(loss="binary_crossentropy",optimizer="adam",metrics=["accuracy"])
print("training ........................")
H = model.fit(trainX,trainY,validation_data=(testX,testY),class_weight=classWeights,batch_size= 64 ,epochs=15,verbose=1)
print("evaluating....................")
pre = model.predict(testX,batch_size=64)
print(classification_report(testY.argmax(axis=1),pre.argmax(axis=1),target_names=le.classes_))

print("save....")
model.save("./output/weight.hdf5")
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, 15), H.history["loss"], label="train_loss")
plt.plot(np.arange(0, 15), H.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, 15), H.history["acc"], label="acc")
plt.plot(np.arange(0, 15), H.history["val_acc"], label="val_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.show()

