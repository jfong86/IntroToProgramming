#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: November 05, 2019
"""
    Ask the user to specify the input file,
    Ask the user to specify the output file,
    Convert the date column (which is stored as 'YYYYMMDD') to a datetime format recognized by pandas, for example if your dataframe is df, overwrite the 'Date' column to be:

    df["Date"] = pd.to_datetime(df["Date"].apply(str))	

    Make a plot of the percentage of the total population that are children over time from the data in input file, and
    Store the plot in the output file the user specified. 
"""

import pandas as pd
import matplotlib.pyplot as plt

inFile = input('Enter the name of a CSV file here:')
#outFile = input('Enter the name of what you want the CSV file to store as:')

df = pd.read_csv(inFile)
df["Date"] = pd.to_datetime(df["Date"].apply(str))

df.plot(x = "Enrolled", y = "Date")
#print(df["Date"])
