#Declare library and set variable from library
from sys import argv

#Set varibel for argument variables
script, filename = argv

#Prints what is going to happen to variable filename, and how to proceed or not proceed.
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#Input from user whether to proceed or not
raw_input("?")

#Informs user that fille is being opned.
print "Opening the file..."
#Sets variable 'target' to open function for variable 'filename'. The 'w' ensures that we want to write over current file.
target = open(filename, 'w')

#Managing file size?
#print "Truncating the file. Goodbye!"
#target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these files to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print "And finally, we close it."
target.close()
