# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 13:19:06 2017

@author: Satya
"""

import numpy as np
from skimage import io

center=np.load('codebook.npy')


tiger=io.imread('C:\\Users\\Satya\\Desktop\\Python\\compressed_image2.png')

x= tiger.shape[0]
y= tiger.shape[1]
image=np.zeros(shape=(x,y,3),dtype='uint8')
#print image.dtype
for i in range (1,x):
    for j in range (1,y):
        image[i,j]=center[tiger[i,j]]
image=image.reshape(x,y,3)
print image.dtype,image.shape
io.imsave('reconstructed_image3.png',image)
io.imshow(image)