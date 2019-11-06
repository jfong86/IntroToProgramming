#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: September 24, 2019
"""
prompts the user to enter a list of names. 
Each person's name is separated from the next by a semi-colon and a space ('; ') 
and the names are entered lastName, firstName (i.e. separated by ', '). 
Your program should then print out the names, one per line, 
with the first initial of the first name, followed by ".", and followed by the last name.
"""

name = input ("Please enter your list of names: ")
words = name.split('; ')


print ("You entered: " )

for i in words:
    tempName = i.split(', ')
    lastName = tempName[0]
    firstName = tempName[1][0]
    print(firstName+'.',lastName)

print("Thank you for using my name organizer!")