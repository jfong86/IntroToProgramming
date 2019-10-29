#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: September 10, 2019
#This program prompts the user to enter a phrase 
#and then prints out the ASCII code of each character in the phrase.

mess = input("Enter a phrase:")
#print(mess)

for c in mess:
    print(ord(c))
