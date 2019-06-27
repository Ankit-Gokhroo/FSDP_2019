# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 23:24:31 2019

@author: Ankit Gokhroo
"""
"""
GIF Creator

A program that puts together multiple images (PNGs, JPGs, TIFFs) to make a smooth 
GIF that can be exported. Make the program convert small video files to GIFs as 
well.
"""

from PIL import Image, ImageDraw

def create_image(length,width,x,y):
    img = Image.new('RGB', (400,400), color = 'yellow')
    draw = ImageDraw.Draw(img)
    draw.rectangle((length,width,x,y),fill=(0,0,0))
    return img


# Create the frames
frames = []
x, y = 0, 0
for i in range(10):
    new_frame = create_image(40,40,x,y)
    frames.append(new_frame)
    x += 40
    y += 40
    
    
# Save into a GIF file that loops forever
frames[0].save('rect.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)




]








