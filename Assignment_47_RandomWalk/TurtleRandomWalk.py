#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: Nov. 13, 2019
#This program use a Turtle library to draw a "random walk" turtle

import turtle
import random

ninjaTurtle = turtle.Turtle()
ninjaTurtle.speed(10)

for i in range(100):
    ninjaTurtle.forward(30)
    a = random.randrange(0,350,10)
    ninjaTurtle.right(a)
