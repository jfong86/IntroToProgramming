#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: September 24, 2019
"""
This program asks the user for a message and then 
prints the message out, three copies of one character per line.
"""

myString = input("Enter a message: ")

for alice in myString:
    print(alice, alice, alice)