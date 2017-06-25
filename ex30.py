# sets variable for people
people = 30
# sets variable for cars
cars = 40
# sets variable for trucks
trucks = 15

# boolean expression to follow if True
if cars > people:
# block to run if above boolean is True
    print "We should take cars."
# boolean expression to follow if True
elif cars < people:
# block to run if above boolean is True
    print "We should not take cars."
# boolean expression to follow if True
else:
# block to run if above boolean is True
    print "We can't decide."

# boolean expression to follow if True
if trucks > cars:
# block to run if above boolean is True
    print "That's too many trucks."
# boolean expression to follow if True
elif trucks < cars:
# block to run if above boolean is True
    print "Maybe we could take trucks."
# boolean expression to follow if True
else:
# block to run if above boolean is True
    print "We still can't decide."

# boolean expression to follow if True
if people > trucks:
# block to run if above boolean is True
    print "Alright, let's just take the trucks."
# boolean expression to follow if True
else:
# block to run if above boolean is True
    print "Fine, let's stay home then."

