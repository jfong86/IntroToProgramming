#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: October 10, 2019
"""Write a program that implements the pseudocode below:

    For i = 90, 88, 86, 84, 82, ... ,0:
        Walk forward 25 steps
        Turn left i degrees
"""

import turtle;

alice = turtle.Turtle();

for i in range (90, 0, -2):
    alice.forward(25)
    alice.left(i)