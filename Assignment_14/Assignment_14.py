#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: September 15, 2019
#This program write a program that creates a 'C' logo for CUNY on a 30x30 grid

import matplotlib.pyplot as plt #import libraries for plotting
import numpy as np #and for arrays (to hold images)
logoImg = np.ones((30,30,3)) #10x10 array with 3 sheets of 1’s

logoImg[:,:,:2] = 0
logoImg[10:20,10:,0:2] =1

plt.imshow(logoImg)
plt.show()
#plt.imsave("logo.png", logoImg)