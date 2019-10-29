#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: Oct. 28, 2019
"""
displays shelter population over time to:

    ask the user to specify the input file,
    ask the user to specify the output file,
    make a plot of the fraction of the total population that are children over time from the data in input file, and
    store the plot in the output file the user specified. 
"""

import pandas as pd
import matplotlib.pyplot as plt

fileName = input("Enter name of input file: " )
outFile = input("Enter name of output file: " )

homeless = pd.read_csv(fileName)
homeless['Fraction Children'] = homeless['Total Children in Shelter']/homeless['Total Individuals in Shelter']
homeless.plot(x = "Date of Census", y = "Fraction Children")
#plt.show()

abcd = plt.gcf()
abcd.savefig(outFile)
