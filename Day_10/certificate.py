# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 11:43:16 2019

@author: Ankit Gokhroo
"""

#function for creating certificate

def certificate(a,b,c,e,z):
    """taking name,training title,start date,end date as a arguements
    all should in correct format
    """
    #creating new image
    img = Image.new('RGB', (800, 600), color = 'white')
    #selecting font for image
    fnt = ImageFont.truetype('C:/Windows/Fonts/CASTELAR', size=45)
    
    d = ImageDraw.Draw(img)
    
    #writing text on image
    d.text((40,60), "CERTIFICATE OF COMPLETION", fill=(0,0,0),font=fnt)

    fnt1 = ImageFont.truetype('C:/Windows/Fonts/AdobeFangsongStd-Regular', size=25)
    d.text((250,150), z , fill=(0,0,0),font=fnt1)


    fnt1 = ImageFont.truetype('C:/Windows/Fonts/AdobeFangsongStd-Regular', size=40)
    d.text((300,200), a , fill=(200,200,100),font=fnt1)

    d.text((50,240), " successfully completed the training of ", fill=(0,0,0),font=fnt1)

    d.text((180,300), b, fill=(200,200,100),font=fnt1)
        
    d.text((150,360), "at FORSK TECHNOLOGIES", fill=(0,0,0),font=fnt1)

    d.text((100,420), "from "+c+" to "+e, fill=(0,0,0),font=fnt1)

    img2 = Image.open("forskpic.png")
    
    #resizing the image
    small_im = img2.resize((100,93), resample=Image.BICUBIC)
    small_im.save('small_sample1.png')
    offset=(340,500)

    img1=Image.open("small_sample1.png")  
    
    #paste a other image in our image
    img.paste(img1,offset) 

    fnt2 = ImageFont.truetype('C:/Windows/Fonts/AdobeFangsongStd-Regular', size=20)
    d.text((100,550),"COORDINATOR", fill=(0,0,0),font=fnt2)

    d.text((550,550),"FOUNDER", fill=(0,0,0),font=fnt2)

    d.text((70,530),"---------------------------------", fill=(0,0,0),font=fnt2)

    d.text((510,530),"----------------------------------", fill=(0,0,0),font=fnt2)

    d.text((500,520),"SYLVESTER FERNENDES", fill=(0,0,0),font=fnt2)

    d.text((80,520),"YOGENDRA SINGH", fill=(0,0,0),font=fnt2)

    img.save('certificate.png')

    img = Image.open('certificate.png')
    bimg = ImageOps.expand(img, border=10, fill='black')

    bimg.save('certificate2.png')
    
    
#importing modules    
import os
from PIL import Image, ImageDraw, ImageFont
from PIL import Image, ImageOps
import re

#taking user information

name=input('enter your name')
name=name.upper()
title=input('enter your title of training')
title=title.upper()
start_date=input('enter start date in date month and yaer sequence sepearated by space like"12 01 2012"')
start_date=start_date.replace(' ','-')
end_date=input('enter end date in date month and yaer sequence sepearated by space like "12 03 2019"')
end_date=end_date.replace(' ','-')
z="THIS IS AWARDED TO"



if re.findall(r'\d{2}\-\d{2}\-\d{4}',start_date and end_date): 
     certificate(name,title,start_date,end_date,z)
else:
    print ('information is invalid ')
    


