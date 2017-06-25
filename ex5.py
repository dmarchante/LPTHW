name = 'David Marchante'
age = 35 # not a lie
height = 68.0 # inches
cm_conv = 2.54
height_cm = height * cm_conv
weight = 175.0 # lbs
kg_conv = 2.2
weight_kg = weight * kg_conv
eyes = 'Brown'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall, or %d centimeters." % (height, height_cm)
print "He's %d pounds heavy, or %d kilograms." % (weight, weight_kg)
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the cofee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
