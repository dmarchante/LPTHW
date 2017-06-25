def add(a, b):
    print "Adding %d to %d = " % (a, b)
    return a + b

def multiply(a, b):
    print "Multiplying %d by %d = " % (a, b)
    return a * b

def subtract(a, b):
    print "Subtracting %d from %d = " % (a, b)
    return a - b

def division(a, b):
    print "Dividing %d by %d = " % (a, b)
    return a / b

total = add(7, 3)
product = multiply(5, 2)
difference = subtract(12, 2)
quotient = division(200, 20)

print "Total: %d, Product: %d, Difference: %d, Quotient: %d" % (total, product, difference, quotient)

formulaic = add(total, multiply(product, subtract(difference, division(quotient, 5))))

print "The formulaic result is %d" % (formulaic)
