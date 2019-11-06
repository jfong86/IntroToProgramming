#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: September 24, 2019
#This program asked the user to enter a number in seconds,
#then converts it to Hours, Minutes, and Seconds

timeInSeconds = input("Enter number of seconds: ")
time = int(timeInSeconds)
hours = time // 3600
remainingSeconds = time % 3600
minutes = remainingSeconds // 60
print("Hours: ", hours)
print("Minute: ", minutes)
print("Seconds: ", remainingSeconds % 60)