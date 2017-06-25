# imprt from library
from sys import argv

# set variables for argument variabel
script, input_file = argv

# creates funtion to print complete file specified in argument
def print_all(f):
# directs function to read file specified in argument
    print f.read()

# creates funtion to rewind file specified in argument
def rewind(f):
# directs to rewind file back to 0 byte (beginning)
    print f.seek(0)

# creates function to print line count and line in argument
def print_a_line(line_count, f):
# directs to print line count and specified line
    print line_count, f.readline()

# sets variable to the open "input file"
current_file = open(input_file)

# returns what is currently being output
print "First let's print the whole file:\n"

# prints entire current file via print_all function
current_file.print_all()

# returns what is happening during rewind function
print "Now let's rewind, kind of like a tape."

# rewinds file to beginning of file
rewind(current_file)

# returns what is being output
print "Let's print three lines:"

# sets variable to first line
current_line = 1
# outputs the current line number and contents of first line via function
print_a_line(current_line, current_file)

# sets variable to one mare than current line
current_line = current_line + 1
## outputs the current line number and contents of first line via function
print_a_line(current_line, current_file)

# sets variable to one mare than current line
current_line = current_line + 1
# outputs the current line number and contents of first line via function
print_a_line(current_line, current_file)
