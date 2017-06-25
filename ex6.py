# Declaring variables for joke.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who %s and those who %s." % (binary, do_not)

# Joke output.
print x
print y

# Reiteration of joke.
print "I said: %r." % x
print "I also said: '%s'." % y

# Setting varilbles for joke evaluation.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Print joke evaluation result.
print joke_evaluation % hilarious

# Setting variables for string concatation
w = "This is the left side of..."
e = "a string with a right side."

# Output of string concatation.
print w + e
