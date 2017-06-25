def whileLoop(num, interval):
    i = 0
    numbers = []

    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)

        i += interval
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

whileLoop(11, 5)

whileLoop(21, 3)
