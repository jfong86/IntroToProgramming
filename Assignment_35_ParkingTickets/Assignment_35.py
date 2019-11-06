#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: Oct. 29, 2019
"""
 Modify the parking ticket program from Lab 7 to do the following:

    Ask the user for the name of the input file.
    Ask the user for the attribute (column header) to search by.
"""

#Import pandas for reading and analyzing CSV data:
import pandas as pd

#csvFile = "tickets.csv"             #Name of the CSV file
csvFile = input('Enter CSV file name: ')
attribute = input('Enter attribute: ')
tickets = pd.read_csv(csvFile)      #Read in the file to a dataframe
#print(tickets)                      #Print out the dataframe

#print(tickets["Plate ID"])	#Print out licence plates

#Print out plates & number of tickets each got
#print(tickets["Plate ID"].value_counts())

#Print 10 worst & number of tickets
print("The 10 worst offenders are:")
print(tickets[attribute].value_counts()[:10])  #Print out the data with "10 in the upper limit" or "10 most data" in the dataframe
