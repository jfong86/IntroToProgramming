#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: September 10, 2019
#This program prompts the user for a DNA string, 
#and then prints the length and GC-content 
#(percent of the string that is C or G, written as a decimal).

DNA_string = input("Enter a DNA string:")
DNA_string_length = len(DNA_string)
count_g = DNA_string.count('G')
count_c = DNA_string.count('C')
gc = (count_g + count_c) / DNA_string_length
gcPercent = gc * 100
print("Length is", len(DNA_string))
print("GC-content is", gc)