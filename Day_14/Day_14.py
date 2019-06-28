"""
Histogram
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

plt.hist(data)

plt.hist(data, normed=True, bins=30)

plt.hist(data, bins=30, normed=True, alpha=0.5,
         histtype='stepfilled', color='steelblue',
         edgecolor='red');
         

         
"""
2D plotting with matplotlib
"""

import matplotlib.pyplot as plt
import numpy as np
 
t = np.arange(0.0, 20.0, 0.01)
s = np.sin(t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('A nice sine wave')
plt.grid(True)
plt.savefig('sinewave.png')
plt.show()

"""
Showing bubbles
"""

import numpy as np 
import matplotlib.pyplot as plt 

# Define the number of values
num_vals = 40

# Generate random values
x = np.random.rand(num_vals)
y = np.random.rand(num_vals)

# Define area for each bubble
# Max radius is set to a specified value
max_radius = 25
area = np.pi * (max_radius*np.random.rand(num_vals)) ** 2

# Generate colors
colors = np.random.rand(num_vals)

# Plot the points
plt.scatter(x, y, s=area, c=colors, alpha=.5)
plt.show()


"""
Showing bubbles 2
"""
import numpy as np 
import matplotlib.pyplot as plt 

rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar() # show color scale
# In this way, the color and size of points can be used to convey information in the visualization, 
# in order to visualize multidimensional data.


"""
Box Plot
"""
"""
import numpy as np 
import matplotlib as mpl 
import matplotlib.pyplot as plt 

## agg backend is used to create plot as a .png file
mpl.use('agg')         
         
## Create data
np.random.seed(10)
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)
collectn_4 = np.random.normal(70, 25, 200)

## combine these different collections into a list    
data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]

# Create a figure instance
fig = plt.figure(1, figsize=(9, 6))

# Create an axes instance
ax = fig.add_subplot(111)

# Create the boxplot
bp = ax.boxplot(data_to_plot)


fig.savefig('fig1.png', bbox_inches='tight')

"""




              
"""
# Showing Different ways of Scatter Plots with plot
# Convert the random function from random class

import numpy as np
import matplotlib.pyplot as plt 
rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
             label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8);
"""


"""
More on box ploting to identify the outliers
"""

# https://plot.ly/create/box-plot/
# Define box plot with Gate Example
# Relative Performance
# 4 Quartiles

import numpy as np

incomes = np.random.normal(27000, 15000, 10000)
np.mean(incomes)
np.median(incomes)
np.std(incomes)

#We can segment the income data into 20 buckets, and plot it as a histogram:

import matplotlib.pyplot as plt
plt.hist(incomes, 20)
plt.show()

plot = plt.boxplot(incomes)


#box and whisker plot to show distribution
#https://chartio.com/resources/tutorials/what-is-a-box-plot/
#box plot creating: https://plot.ly/create/box-plot/#/
incomes = np.append(incomes,100000)
plot = plt.boxplot(incomes)


#second version

import pandas as pd
import numpy as np

incomes = np.random.normal(27000, 15000, 10000)
bp= pd.DataFrame.boxplot(pd.DataFrame(incomes), return_type='dict')

outliers = [flier.get_ydata() for flier in bp["fliers"]]
boxes = [box.get_ydata() for box in bp["boxes"]]
medians = [median.get_ydata() for median in bp["medians"]]
whiskers = [whiskers.get_ydata() for whiskers in bp["whiskers"]]

"""
removing outlies from the incomes
xx = [item for item in incomes if (item > -13124 and item < 67665)]
you get the min and max values from whiskers

"""


"""
return_type : {‘axes’, ‘dict’, ‘both’} or None, default ‘axes’
The kind of object to return. The default is axes.

‘axes’ returns the matplotlib axes the boxplot is drawn on.

‘dict’ returns a dictionary whose values are the matplotlib Lines of the boxplot.

‘both’ returns a namedtuple with the axes and dict.
http://colingorrie.github.io/outlier-detection.html

"""
"""
https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba
"""

#---------------------------------------
#Standard Deviation, Variance, Mode, Frequency Table

import numpy as np
import matplotlib.pyplot as plt

incomes = np.random.normal(100.0, 50.0, 10000)
#incomes = np.random.normal(27000.0, 15000.0, 10000)
plt.hist(incomes, 50)
plt.show()

print (incomes.std())
print (incomes.var())
#The standard deviation is the square root of the variance. 


randNumbers = np.random.randint(5,15,40)
counts = np.bincount(randNumbers)
print (np.argmax(counts))



#################


from numpy import genfromtxt
#to read as record array
my_data = genfromtxt('Salaries.csv', delimiter=',', dtype=None)



###################











"""
Other Advanced Operations on NumPy  Arrays
"""

one_d_array = np.array([1,2,3,4,5,6])
print (one_d_array)

# Create a new 2d array
two_d_array = np.array([one_d_array, one_d_array + 6, one_d_array + 12])
print(two_d_array)

# Slice elements starting at row 2, and column 5
two_d_array[1:, 4:]

# Reverse both dimensions (180 degree rotation)
two_d_array[::-1]
two_d_array[:,::-1]
two_d_array[::-1, ::-1]

#Reshaping an Array
np.reshape(a=two_d_array,        # Array to reshape
           newshape=(6,3))       # Dimensions of the new array

#Unravel a multi-dimensional into 1 dimension with np.ravel():
np.ravel(a=two_d_array,
         order='C')         # Use C-style unraveling (by rows)

np.ravel(a=two_d_array,
         order='F')         # Use Fortran-style unraveling (by columns)


#Alternatively, use ndarray.flatten() to flatten a multi-dimensional into 1 dimension and return a copy of the result:
two_d_array.flatten()


#Transpose of the array
two_d_array.T


#Flip an array vertically np.flipud(), upside down :
np.flipud(two_d_array)

  
#Flip an array horizontally with np.fliplr(), left to right:
np.fliplr(two_d_array)


#Rotate an array 90 degrees counter-clockwise with np.rot90():
np.rot90(two_d_array,
         k=2)             # Number of 90 degree rotations
 

#Shift elements in an array along a given dimension with np.roll():
np.roll(a= two_d_array,
        shift = 2,        # Shift elements 2 positions
        axis = 1)         # In each row

np.roll(a= two_d_array,
        shift = 2,        # Shift elements 2 positions
        axis = 0)         # In each columns

#Join arrays along an axis with np.concatenate():
array_to_join = np.array([[10,20,30],[40,50,60],[70,80,90]])

print (array_to_join)

np.concatenate( (two_d_array,array_to_join),  # Arrays to join
               axis=1)                        # Axis to join upon


# Get the mean of all the elements in an array with np.mean()
np.mean(two_d_array)

# Provide an axis argument to get means across a dimension
np.mean(two_d_array,
        axis = 1)     # Get means of each row

# Get the standard deviation all the elements in an array with np.std()
np.std(two_d_array)


# Provide an axis argument to get standard deviations across a dimension
np.std(two_d_array,
        axis = 0)     # Get stdev for each column

# Sum the elements of an array across an axis with np.sum()
np.sum(two_d_array, 
       axis=1)        # Get the row sums

np.sum(two_d_array,
       axis=0)        # Get the column sums

# Take the square root of each element with np.sqrt()
np.sqrt(two_d_array)


# Take the dot product of two arrays with np.dot(). 
# This function performs an element-wise multiply and then a sum for 1-dimensional 
# arrays (vectors) and matrix multiplication for 2-dimensional arrays.
# Take the vector dot product of row 0 and row 1

np.dot(two_d_array[0,0:],  # Slice row 0
       two_d_array[1,0:])  # Slice row 1


"""
Color-image data for single image is typically stored in three dimensions. 
Each image is a three-dimensional array of (height, width, channels), 
where the channels are usually red, green, and blue (RGB) values. 
One 256x256 RGB images would have shape (256, 256, 3). 

(An extended representation is RGBA, where the A–alpha–denotes the level of opacity.)
One 256x256 ARGB images would have shape (256, 256, 4). 


Color-image data for multiple images is typically stored in four dimensions. 
A collection of images is then just (image_number, height, width, channels). 
One thousand 256x256 RGB images would have shape (1000, 256, 256, 3). 

"""
 



from skimage import io

photo = io.imread('hawa_mahal.jpg') 


"""
print(type(photo))
print (photo.dtype)
print (photo.itemsize)
print (photo.size) # 147x220x3 = 97020
print (photo.nbytes)
"""


print (photo.ndim)
# height = 147, width = 220 , RBG 
print (photo.shape) #(147, 220, 3)

print (photo)

print(photo[0]) # first layer
print(photo[146]) # Last layer

print(photo[146][0]) # 0th row for the last layer

print(photo[146][0][0]) # RED Component of 0th row for the last layer


import matplotlib.pyplot as plt
plt.imshow (photo)

# Reversed rows
plt.imshow(photo[::-1])

# Revered the columns so we got a mirrored image
plt.imshow(photo[:,::-1])

# Section of the photos
plt.imshow(photo[50:147, 150:220])

# halved the size of the image
plt.imshow(photo[::2,::2])

#import numpy as np
#photo_sin = np.sin(photo)
#photo_sin

