#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: October 10, 2019
"""Elevation Map

create a topographic map (highlighting the points that have 
elevations that are multiples of 10). Your program should ask 
the user for the amount of blue (a floating point number 
between 0.0 and 1.0), the name of the output imagee, 
create a new image with thaht name and with the pixels colored as follows:

If the elevation is less than or equal to 0, color the pixel the amount blue the user specified (and 0% red and 0% green).
If the elevation is divisible by 10, color the pixel black (0% red, 0% green, and 0% blue).
Otherwise, the pixel should be colored white (100% red, 100% green, and 100% blue).

Program should run like:

How blue is the ocean:  0.5
What is the output file:  medBlue.png
Thank you for using my program!
Your map is stored medBlue.png.

"""

#Import numpy and matplotlib libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt

degreeBlue=input("How blue is the ocean: ", )
fileName=input("What is the output file: " )


elevations = np.loadtxt('elevationsNYC.txt')  #load the array from the text file into matplotlib.pyplot
plt.imshow(elevations)  #load the array into matplotlib.pyplot

#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
           floodMap[row,col,2] = degreeBlue     #Set the blue channel to 100%
        elif elevations[row,col] % 10 == 0:
           floodMap[row,col,0:2] = 0     #Set all (R/G) channel to 0%
        else:
            floodMap[row,col,0:3] = 1.0   #Set all (R/G/B) channels to 100%

#Load the flood map image into matplotlib.pyplot:
plt.imshow(floodMap)

#Display the plot:
plt.show()

#Save the image:
plt.imsave(fileName, floodMap)

print("Thank you for using my program!")
print("Your map is stored ", fileName)