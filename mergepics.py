#!usr/bin/env python
#-*- coding: utf-8 -*-
# merge pictures

import PIL.Image as Image
import os

num = 10
picpxl = 110
#create a new blank image
toImg = Image.new('RGBA', (num * picpxl, num * picpxl), color = 255)

imgpath = r'C:/Users/lu/Desktop/tieba/'
#get the list of image's name
imglist = os.listdir(imgpath)

for row in range(num):
    for column in range(num):
        srcImg = Image.open(imgpath + imglist[row * num + column])
        toImg.paste(srcImg, (column * picpxl, row * picpxl))
        
toImg.save('mergepics.jpg')

"""
.paste(i2,where,mask=None)
Pixels are replaced with the pixels from image i2.
Where is a pair of coordinates (x,y).
If where is None,  i2 must be the same size as the original.
"""

        
