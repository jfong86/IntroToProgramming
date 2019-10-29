#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: September 10, 2019
#This program prompts the user to enter a word 
#and then prints out the word with each letter shifted right by 13.

#Example: That is, 'a' becomes 'n', 'b' becomes 'o', ... 'y' becomes 'l', and 'z' becomes 'm'.

word = input("Enter a word:")
new_Word = ""

for letter in word:

    if (ord(letter) > 96 and ord(letter) < 123):
        offset = ord(letter) - ord('a') + 13  #How many letters past 'a'
        #If larger than 26, wrap back to the letter 'a', which is the 97th position.
        wrap_back = offset % 26   
        new_Char = chr(ord('a') + wrap_back)
        #print (wrap_back, chr(ord('a') + wrap_back))  #Print the wrap & new letter
        new_Word = new_Word + new_Char  #Add the new_Char to the new_Word

    else:
       offset = ord(letter) - ord('A') + 13  #How many letters past 'a'
       wrap_back = offset % 26  #If larger than 26, wrap back to 0
       new_Char = chr(ord('A') + wrap_back)  #Compute the new letter
        #print (wrap_back, chr(ord('a') + wrap_back))  #Print the wrap & new letter
       new_Word = new_Word + new_Char  #Add the new_Char to the new_Word

print(new_Word)


