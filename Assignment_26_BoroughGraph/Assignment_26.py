#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: October 16, 2019
"""
This program import the 'NYC historical population data (nycHistPop.csv)', 
then ask the user for the borough, an name for the output file, 
and then display the fraction of the population that has lived in that borough, over time."""

import matplotlib.pyplot as plt
import pandas as pd

borough=input("Enter borough name: ", )
fileName=input("Enter output file name: ", )

#created a variable "pop" and import the nycHistPop.csv data in Pandas
#The nycHistPop.csv data has 5 extra lines at the top before the column names occur.
#The pandas function for reading in CSV files is read_csv(). 
#It has an option to skip rows which we will use here.
pop = pd.read_csv('nycHistPop.csv', skiprows=5)
#print(pop)

#pop.plot(x="Year")
#plt.show()

#print(pop['Bronx'])
#print(pop['Bronx']*2)
#print(pop['Bronx']/pop['Total'])
#pop['Fraction'] = pop['Bronx']/pop['Total']

pop['Fraction']=pop[borough]/pop['Total']
pop.plot(x='Year', y='Fraction')
#plt.show()

#We can save it to a file, by storing the current figure via "get current figure" or 
#gcf() function and then saving it:
fig=plt.gcf()
fig.savefig(fileName)