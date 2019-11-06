#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: September 27, 2019
#This program draws an octagon (8-sided polygon)

import turtle

Alice = turtle.Turtle()

for i in range(8):
    Alice.forward(50)
    Alice.left(360/8)