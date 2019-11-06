#Name: Joey Fong
#Email: joey.fong39@myhunter.cuny.edu
#Date: September 10, 2019
#This program asks the user for a noun and two verbs
#Using the words the user entered, print out a new sentence of the form:

#If it VERB1 like a NOUN and VERB2 like a NOUN, it probably is a NOUN.

##Example:
##Enter a noun: duck
#Enter a verb: walks
#Enter another verb: talks

#New sentence:
#If it walks like a duck and talks like a duck, it probably is a duck.

#New_Sentence = "If is Verb1 like a Noun and Verb2 like a Noun, it probably is a Noun."

noun = input("Enter a noun:")
verb1 = input("Enter a verb:")
verb2 = input("Enter another verb:")

string = "If it VERB1 like a NOUN and VERB2 like a NOUN, it probably is a NOUN."
string = string.replace("NOUN", noun)
string = string.replace("VERB1", verb1)
string = string.replace("VERB2", verb2)
print(string)