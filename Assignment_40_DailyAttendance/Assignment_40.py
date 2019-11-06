#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: November 05, 2019
"""
    
    Ask the user to specify the input file,
    Ask the user to specify the output file,
    Convert the date column (which is stored as 'YYYYMMDD') to a datetime format recognized by pandas, for example if your dataframe is df, overwrite the 'Date' column to be:

    df["Date"] = pd.to_datetime(df["Date"].apply(str))	

    Make a plot of the percentage of those who attended over time from the data in input file, and
    Store the plot in the output file the user specified. 
"""

import pandas as pd #import pandas library
import matplotlib.pyplot as plt #import matplotlib-pyplot library

inFile = input('Enter the name of a CSV file here:') #read file
outFile = input('Enter the name of the file to store as:')

df = pd.read_csv(inFile) #read CSV file in pandas

df["Date"] = pd.to_datetime(df["Date"].apply(str)) #convert date into string

#percentage of (student present / student enrolled in school)
df["% Attending"]=(df["Present"]/df["Enrolled"])*100

#plot the data into graph
df.plot(x = "Date", y = "% Attending")
#plt.show()
#print(df["Date"])

attendanceGraph = plt.gcf()
attendanceGraph = plt.savefig(outFile)
