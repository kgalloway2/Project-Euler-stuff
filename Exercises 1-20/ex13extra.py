from sys import argv

one, two, three, four, five = argv

print "This is the first variable: ", one
print "This is the second variable: ", two
print "The third: ", three
print "Fourth: ", four
print "What should we change the fifth to?",
print "It was %r. Now it is %r" % (five, raw_input('New variable: '))