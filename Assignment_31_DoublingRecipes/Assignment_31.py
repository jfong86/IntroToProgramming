#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: October 22, 2019
"""
program that asks the user for a recipe (in comma separated value (CSV) format),
reads in the corresponding CSV file and prints out quantities and ingredients needed to make a double batch.
Assume that the CSV files have the columns: "Amount", "Measurement", and "Ingredient".4
"""
import pandas as pd

fileName=input("Enter recipe name: ", )

a = pd.read_csv(fileName)

a['Amount'] = a['Amount']*2

print(a)

#print("Double your recipe is: ", )
