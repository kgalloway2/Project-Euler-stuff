name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
cf_in_cm = 2.54
weight = 180 # lbs
cf_lbs_kg = 0.45
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s" % name
print "He's %d inches tall." % height
print "In centimeters, he is %r centimeters tall." % (height * cf_in_cm)
print "He's %d pounds heavy" % weight
print "In kilograms, he is %r kg." % (weight * cf_lbs_kg)
print "Actualy that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d." % (age, height, weight, age + height + weight)
