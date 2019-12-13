#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: September 12, 2019
#This program asks the user for a name of an image .png file and the name of an output file. 
#Your program should create a new image that has only the blue channel of the original image 
#(that is, no green channel)

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

image = input ("Enter name of the input file: ")
image2 = input ("Enter name of the output file: ")

img = plt.imread('csBridge.png')    #Read in image from csBridge.png
#plt.imshow(img)		    #Load image into pyplot
#plt.show()                         #Show the image (waits until closed to continue)

img2 = img.copy()        #make a copy of our image
img2[:,:,0] = 0          #Set the red channel to 0
img2[:,:,1] = 0          #Set the green channel to 0

#plt.imshow(img2)         #Load our new image into pyplot
#plt.show()               #Show the image (waits until closed to continue)

plt.imsave(image2, img2)  #Save the image we created to the file: blueH.png
