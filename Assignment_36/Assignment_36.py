#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: Oct. 29, 2019
"""
Write a program that asks the user for a CSV of the NYC OpenData Film Permits:

Your program should then print out:

    the total number of permits in the file,
    the count of permits for each borough, and
    the five most popular locations (stored in the column: "Parking Held"). 
"""

import pandas as pd

#csvFile = "Film_Permits.csv"
csvFile = input('Enter file name: ')  #Ask user to input the name of the file
permits = pd.read_csv(csvFile)  #Read the file in pandas
#print(csvFile)  #print what the file is
#print(permits)  #print the entire content (dataframe) of the file

#print('There were',len(permits),'film permits.')  #print out the 'count' of length of entries of permits with "Borough" attributes
print('There were',permits['Borough'].count(),'film permits.') #print out the 'count' of number of permits with 'Boroughs' attribute
print(permits['Borough'].value_counts()) #print the number of permits each Borough has

#print() #this print out an empty line

print('\nThe five most popular filming locations were:') #Here, \n means "new line". This will print the statement in the next line.

print(permits['ParkingHeld'].value_counts()[:5]) #Here, we print 5 most parking location with filming permits
