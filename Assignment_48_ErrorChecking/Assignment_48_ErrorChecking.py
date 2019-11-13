#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: Nov. 13, 2019
"""
Write a program that asks the user to enter their age.
If the user enters negative number, your program should continue
prompting the user for a positive number until they enter a one.
Your program should then print out the number entered. 
"""

inputAge = int(input("Enter your age: "))
age = 0
while inputAge < age:
    print("You entered a negative number. Try again.")
    inputAge = int(input("Enter your age: "))
print("You entered: ", inputAge)
