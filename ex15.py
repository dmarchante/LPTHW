#Pulls from library, and asks for argument variables
from sys import argv

#sets argument variables
script, filename = argv

#Sets variable txt to function opening the argument variable 'filename'
txt = open(filename)

#Output of the argument variable 'filename'
print "Here's your file %r:" % filename
#Outputs the contents of the argument variable 'filename', by utilizing the method read for set variable txt
print txt.read()

#Prompts for input of argument variable 'filename',
print "Type the filename again:"
#Set's variable file_again via raw_input function. (Intention is to resubmit previiosly entered filename)
file_again = raw_input("> ")

#Sets variable txt _again to function opening the variable file_again'
txt_again = open(file_again)

#Outputs the contents of the argument variable 'file_again', by utilizing the method read for set variable txt_again
print txt_again.read()
