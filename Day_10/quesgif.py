# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 23:11:42 2019

@author: Ankit Gokhroo
"""
from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageOps

img = Image.new('RGB', (800, 200), color = 'pink')

fnt = ImageFont.truetype('C:/Windows/Fonts/CASTELAR', size=90)
d = ImageDraw.Draw(img)

def a1():
    d.text((40,60), "A", fill=(0,0,0),font=fnt)
    return img
    
def a2():
    d.text((40,60), "A", fill=(0,0,0),font=fnt)
    d.text((120,60), "N", fill=(0,0,0),font=fnt)
    return img
def a3():
    d.text((40,60), "A", fill=(0,0,0),font=fnt)
    d.text((120,60), "N", fill=(0,0,0),font=fnt)
    d.text((200,60), "K", fill=(0,0,0),font=fnt)
    return img
def a4():
    d.text((40,60), "A", fill=(0,0,0),font=fnt)
    d.text((120,60), "N", fill=(0,0,0),font=fnt)
    d.text((200,60), "K", fill=(0,0,0),font=fnt)
    d.text((280,60), "I", fill=(0,0,0),font=fnt)
    return img
def a5():
    
     d.text((40,60), "A", fill=(0,0,0),font=fnt)
     d.text((120,60), "N", fill=(0,0,0),font=fnt)
     d.text((200,60), "K", fill=(0,0,0),font=fnt)
     d.text((280,60), "I", fill=(0,0,0),font=fnt)
     d.text((360,60), "T", fill=(0,0,0),font=fnt)
     return img
        
frames = []
for i in range(5):
    if i==0:
        n=a1()
        frames.append(n)
    if i==1:
        n=a2()
        frames.append(n)
    if i==2:
        n=a3()
        frames.append(n)
    if i==3:
        n=a4()
        frames.append(n)
    if i==4:
        n=a5()
        frames.append(n)

# Save into a GIF file that loops forever
frames[0].save('ex.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)






