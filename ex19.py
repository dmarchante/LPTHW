# defines the function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# returns/prints the argument value for "cheese_count"
    print "You have %d cheeses" % cheese_count
# returns/pritns the argument value for "boxes_of_crackers"
    print "You have %d boxes of crackers!" % boxes_of_crackers
# returns/pritns string
    print "Man that's enough for a party!"
# returns/prints string
    print "Get a blanket. \n"

# defines arguments by assigning value directly
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# sets new variables from script
print "OR, we can use variables from our script:"
# assigns values to variables from scripts
amount_of_cheese = 10
amount_of_crackers = 50

# temporarily defines arguments as variables from script
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# sets arguments by utlizing math
print "We can do the math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# sets arguments utilizing variables and math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
