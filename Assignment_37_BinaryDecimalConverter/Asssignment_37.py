#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: Nov. 04, 2019
"""
 Write a program that implements the pseudcode below. Your program should ask the user for a binary number and print out the corresponding decimal number.

    Ask user for input, and store in the string, binString.
    Set decNum = 0.
    For each c in binString,
        decNum = decNum * 2
        if c is 1, then
            decNum = decNum + 1
    Print decNum
		
"""

binString = input(str("Enter binary number: "))

decNum = 0
for c in binString:
    decNum = decNum * 2
    if c == str(1):
        decNum = decNum + 1

print("Your number in decimal is ", decNum)
