#CSci 127 Teaching Staff
#February 2019
#A program that uses functions to print out months.
#Modified by:  Joey Fong

def num2string(num):
     """
     Takes as input a number, num, and
     returns the corresponding name as a string.
     Examples: num2string(0) returns "zero", num2string(1)returns "one"
     Assumes that input is an integer ranging from 0 to 9
     """
     
     numString = ""
     if num == 0:
          numString = "zero"
     if num == 1:
          numString = "one"
     if num == 2:
          numString = "two"
     if num == 3:
          numString = "three"
     if num == 4:
          numString = "four"
     if num == 5:
          numString = "five"
     if num == 6:
          numString = "six"
     if num == 7:
          numString = "seven"
     if num == 8:
          numString = "eight"
     if num == 9:
          numString = "nine"
     return(numString)

def main():
     nums = input('Enter a multi-digit number: ')
     newStr = ""
     for n in nums:
         word = num2string(int(n))
         newStr = newStr + " " + word
     msg = 'In words, your number is:' + newStr + "."
     print(msg)   


#Allow script to be run directly:
if __name__ == "__main__":
     main()