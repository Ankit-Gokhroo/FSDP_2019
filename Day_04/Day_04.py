# File handling in Python 

file = open("words.txt", "rt")

print (file.name)
print (file.mode )
print (file.closed) 

file.close() 

print (file.closed )

dir(file)

"""
There are four different methods (modes) for opening a file
  "r" - Read
  "a" - Append
  "w" - Write 
  "x" - Create 

In addition you can specify if the file should be handled as binary or text mode
  "t" - Text - Default value. Text mode
  "b" - Binary - Binary mode (e.g. images)

"""


# Exception Handling in File Handling
try:
    file = open("words1.txt",  "rt" )
    print (file.name)
except IOError:
    print ( "File not Found or incorrect path")
except Exception:
    print ( "This is a general exception")
finally:
    print ("this is called always")
    file.close() 



# Context Manager to open the File 
# ( Automatically closes the file after using in the block ) 

with open('words.txt', mode='r') as f :
    # perform your operations within this block 
    pass


with open('words.txt', mode='rt') as file :
   file_contents = file.read()
   print (file_contents)
   
   
with open('words.txt', mode='rt') as file :
   file_contents = file.readline()
   print (file_contents)
   file_contents = file.readline()
   print (file_contents)


with open('words.txt', mode='rt') as file :
   file_contents = file.readlines()
   print (file_contents)


with open('words.txt', mode='rt') as file :
   for line in file:
       print (line)


with open('words.txt', mode='rt') as file :
   file_contents = file.read(4)
   print (file_contents)


file = open("words.txt", "rt")

position = file.tell()
print (position)

line = file.readline()
print (line )

position = file.tell()
print (position)

# The method seek() sets the file's current position at the offset.

   
# file.seek(offset[, whence])
# offset − This is the position of the read/write pointer within the file.
# whence − defaults to 0 which means absolute file positioning,
#          1 which means seek relative to the current position,
#          2 means seek relative to the file's end


line = file.readline()
print (line) 
   
position = file.tell()
print (position)
    
file.seek(0,0) 
position = file.tell()
print (position)

file_contents = file.read(6)
print (file_contents)

position = file.tell()
print (position)

lines = file.readlines()
print (lines)


"""
How to create and write into Files
"""


file = open('new.txt', mode='wt')

file.write("Now this has one line\n")
file.writelines(["Second Line\n", "Third Line\n"])

file.close()



"""
How to read and write non text files
"""


with open ("a.jpg", "rb") as rf :
  with open ("b.jpg", "wb") as wf :
    for line in rf :
      wf.write ( line)



"""
Important Operating System related file handling
"""
      
import os

os.getcwd()

os.chdir("/Users/sylvester/Desktop/Python/data")

os.getcwd()

os.path.exists("zoo.csv")

os.path.exists("data/zoo.csv")


os.remove("new.txt")

os.makedirs("myfolder")

os.rmdir("myfolder")

os.listdir(".")



"""
PIL ( PILLOW LIBRARY )
"""


from PIL import Image
import os

#os.chdir("/Users/sylvester/Desktop/Python/")

# Open the image and create it's instance
img = Image.open("sample1.jpg")

# Gives the dimensions or the size of the image
print (img.size)

# Gives the width of the image
print (img.width)

# Gives the width of the image
print (img.height)


# Gives the format of image like JPEG, PNG ...
print (img.format)

# Gives the mode of image like RGB, binary, GreyScale ...
print (img.mode)

# Displays the Image
img.show()


# Rotate the image with the given angle
# Create separate instance for rotated image
# ROTATE_90, ROTATE_180, ROTATE_270
img_rotate = img.transpose(Image.ROTATE_90)
 
# Displays the rotated image
img_rotate.show()  

img_rotate.save("sample1.jpg")


# Resizing the image 
small_im = img.resize((300, 150), resample=Image.BICUBIC)
small_im.save('small_sample1.jpg')


# Creating Thumbnail
img = Image.open("sample.jpg")
img.thumbnail((150, 100))
print(img.width, img.height)
img.save('thumb_sample1.jpg')


# Cropping
img = Image.open("sample.jpg")
                    # startx, starty,width,height
crop_im = img.crop(box=(340, 20, 560, 164))
crop_im.save('crop_sample1.jpg')


# Adding a Border

img = Image.open("sample.jpg")
border_im = Image.new('RGB', (img.width+20, img.height+20), 'yellow')
border_im.paste(img, (10, 10))
border_im.save("data/border_sample.jpg")


# Flip the image
# Create separate instance for flipped image
# FLIP_LEFT_RIGHT, FLIP_TOP_BOTTOM
img_flip = img.transpose(Image.FLIP_TOP_BOTTOM)

# Displays the rotated image
img_flip.show()  
img_flip.save("sample2.jpg")



# Make Black and White image
img_bw = Image.open("sample.jpg")
img_bw.convert(mode='L').save('sample3.jpg')
img_bw = Image.open("sample3.jpg")
img_bw.show()


# Blur the Images 
from PIL import Image, ImageFilter
img_blur = Image.open("sample1.jpg")

# 15 is the radius, default is 2 so it doesn’t show too much 
img_blur.filter(ImageFilter.GaussianBlur(15)).save('sample4.jpg')
img_blur = Image.open("sample4.jpg")
img_blur.show()



"""
Playing with csv files
"""



"""
For example, you might export the results of a data mining program to a CSV 
file and then import that into a spreadsheet to analyze the data, generate 
graphs for a presentation, or prepare a report for publication.


A CSV file (Comma Separated Values file) is a type of plain text file 
that uses specific structuring to arrange tabular data.

Because it's a plain text file, it can contain only actual text data
—in other words, printable ASCII or Unicode characters.

Normally, CSV files use a comma to separate each specific data value.

In general, the separator character is called a delimiter, 
and the comma is not the only one used.
Other popular delimiters include the tab (\t), colon (:) and semi-colon (;).
 
"""

    
import csv

with open("Salaries.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # row has the list of all columns
    for row in csv_reader:
        print (row)
     
 
# Printing  a specific column    
import csv

with open("Salaries.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # row has the list of all columns
    for row in csv_reader:
        print ( row[0] )
      

    
# Skipping a header line or first line
        
import csv

with open("Salaries.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Skip the first row
    next(csv_reader)
    # row has the list of all columns
    for row in csv_reader:
        print (row)

        
        
# Reading as a Dictionary
        
import csv

with open("Salaries.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        print ( row )
        #print ( row['discipline'] )
        #print ( row['salary'] )
        #print ( row['service'] )
        #print ( row['rank'] )
        #print ( row['sex'] )
        #print ( row['phd'] )



"""
Creating a csv file
"""

        
import csv

with open('employee.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',')

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])


