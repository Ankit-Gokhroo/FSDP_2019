# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 10:28:54 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Image Processing using PIL
  Filename: 
    imgprocess.py
  Problem Statement:
    Given an image, perform image processing operations. 

    Keep only one output image i.e perform all tasks on the same image (override) 
    and print only the name of your output image with extension name in the end of your program. 

    Take the Image name from User (Handle the extension for image file name in your code)
    
    The image processing features to be provided by your code are:

        a.     Greyscale
        b.     Rotate_90 (Rotate the given image file by 90 clockwise)
        c.     Crop (Center) (size = 160(W), 204(H))
        d.     Thumbnail – Generate the thumbnail of the given image (size = 75, 75)
    
"""


from PIL import Image
import os

img = Image.open("sample.jpg")

print(img.width)
print(img.height)


img_rotate = img.transpose(Image.ROTATE_90)
img_rotate.show()

i=img.rotate(90)


img = Image.open('sample.jpg').convert('LA')
img.save('greyscale.png')
img.show()


img = Image.open("sample.jpg")
                    # startx, starty,width,height
crop_im = img.crop(box=(340, 20, 160, 204))
crop_im.save('crop_sample1.jpg')



img_rotate.thumbnail((75,75))
img_rotate.show()
