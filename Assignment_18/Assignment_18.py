#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: September 24, 2019
"""
This program asks the user for 5 whole (integer) numbers. 
For each number, turn the turtle left the degrees entered and 
then the turtle should move forward 100.
"""

import turtle
draw = turtle.Turtle()

for time in range (5):
    a = int(input("Enter a number: "))
    draw.left(a)
    draw.forward(100)