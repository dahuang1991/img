# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:29:05 2017

@author: Satya
"""

import numpy as np
from skimage import io
from sklearn.cluster import DBSCAN

tiger=io.imread('C:\\Users\\Satya\\Desktop\\Python\\parrot4.png')
#print tiger.dtype
io.imshow(tiger)

x= tiger.shape[0]
y= tiger.shape[1]



tiger=tiger.reshape(x*y,3)
#print tiger.shape


dbscan = DBSCAN(eps=0.5).fit(tiger)
label= dbscan.labels_
#center= kmeans.cluster_centers_
print label[200:250]
#print center.shape
print np.unique(label),np.unique(label).shape

#label=np.asarray(label,dtype=np.uint8)
#center=np.asarray(center,dtype=np.uint8)

#np.save('codebook.npy',center)
label=label.reshape(x,y)
io.imsave('compressed_image3.png',label)
image=np.zeros(shape=(x*y,3),dtype='uint8')
for i in range (1,x*y):
    center[i]=label[i]/i
    label[i]=label[i]      


#print image.dtype
#for i in range (1,x*y):
#    image[i]=center[label[i]]
#image=image.reshape(x,y,3)

#io.imsave('reconstructed_image(255).png',image)
#io.imshow(image)
    
    
 