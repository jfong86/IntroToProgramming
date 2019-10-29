#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: August 27, 2019
#This program draws the following pseudocode:

    #Repeat 36 times:
    #    Walk forward 100 steps
    #    Turn left 55 degrees
    #    Walk forward 10 steps
    #    Turn left 55 degrees
    #    Walk forward 100 steps

import turtle

Michelle = turtle.Turtle()

for i in range (36):
    Michelle.forward(100)
    Michelle.left(55)
    Michelle.forward(10)
    Michelle.left(55)
    Michelle.forward(100)